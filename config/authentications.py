from drf_spectacular.extensions import OpenApiAuthenticationExtension 

from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from django.utils.translation import gettext_lazy as _

from users.models import User


class TelegramUserIDAuthenticationExtension(OpenApiAuthenticationExtension):
    target_class = 'config.authentications.TelegramUserIDAuthentication'  # full import path to your auth class
    name = 'TelegramUserIDAuthentication'  # name used in the OpenAPI schema

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'header',
            'name': 'TELEGRAM-USER-ID',  # The header key that your authentication class expects
            'description': 'Telegram user ID to authenticate requests',
        }


class TelegramUserIDAuthentication(BaseAuthentication):
    """
    Custom authentication class that expects a 'TELEGRAM_USER_ID' key in the headers.
    """
    def authenticate(self, request):
        telegram_user_id = request.headers.get('TELEGRAM-USER-ID', "7315758175")

        if not telegram_user_id:
            return None  # No authentication credentials provided, continue

        try:
            # Try to get or create the user with the provided 'user_id'
            user, created = User.objects.get_or_create(id=telegram_user_id)
        except Exception as e:
            print("🔥🔥🔥🔥 Exception = ", e)
            raise AuthenticationFailed(_('Invalid user ID')) from e

        # Attach the user to the request
        return (user, None)