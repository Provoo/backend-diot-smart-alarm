from django.apps import AppConfig

class MilkusersConfig(AppConfig):
    name = 'MilkUsers'

    def ready(self):
        import MilkUsers.signals
