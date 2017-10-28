# -*- coding: utf-8 -*-
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def client(self):
        return ClientUser.objects.filter(user=self).first().client


class Client(models.Model):
    name = models.CharField(max_length=255)


class ClientUser(models.Model):
    user = models.ForeignKey(User)
    client = models.ForeignKey(Client)
