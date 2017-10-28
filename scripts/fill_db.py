import os
import sys

import django

sys.path.insert(0, os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'
django.setup()

from web.models import User, Client, ClientUser


if __name__ == '__main__':
    user = User.objects.get(email='admin@adminov.com')
    client = Client.objects.create(name='OOO Administration')
    ClientUser.objects.create(user=user, client=client)
