from django.apps import AppConfig


class BuzTokenConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "buz_token"

    def ready(self) -> None:
        import buz_token.signals # noqa
