from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = "user_profile"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        import user_profile.signals
