from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.core.signals import setting_changed
        from users.signals import user_post_save

        setting_changed.connect(user_post_save)
