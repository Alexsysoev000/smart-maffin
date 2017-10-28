import logging
from django.apps import AppConfig
from django.conf import settings


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        from web.models import User

        for user_dict in settings.DEFAULT_USERS:
            try:
                User.objects.get(email=user_dict['email'])
            except User.DoesNotExist:
                default_user = User(**user_dict)
                default_user.set_password(user_dict['password'])
                default_user.save()
            except Exception as e:
                logging.error(f'CANT GET USER [{type(e)}] {e}')
