# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME

from web.models import User

logger = logging.getLogger(__name__)


class LoginRequiredView(View):
    login_url = settings.LOGIN_URL

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        return super().dispatch(request, *args, **kwargs)


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/base')
        else:
            return redirect('/login')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/base')
        return render(request, 'web/login.html')

    def post(self, request, redirect_field_name=REDIRECT_FIELD_NAME):
        def error(error_text):
            return JsonResponse({'error': error_text}, status=401)

        redirect_to = request.POST.get(redirect_field_name, settings.LOGIN_REDIRECT_URL)
        # Ensure the user-originating redirection url is safe.
        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = settings.LOGIN_REDIRECT_URL

        if 'email' not in request.POST:
            return error('Требуется email')
        if 'password' not in request.POST:
            return error('Требуется пароль')

        email = request.POST['email'].strip().lower()
        password = request.POST['password']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return error('Email указан неверно')

        user = authenticate(email=email, password=password)
        if user is None:
            return error('Неверный пароль')

        login(request, user)
        return JsonResponse({'redirect_url': redirect_to})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class BaseView(LoginRequiredView):
    def get(self, request):
        return render(request, 'base.html')