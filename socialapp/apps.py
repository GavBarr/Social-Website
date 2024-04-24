from django.apps import AppConfig


class SocialappConfig(AppConfig):
    name = 'socialapp'

    def ready(self):
        import socialapp.signals



