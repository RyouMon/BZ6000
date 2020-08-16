from django.apps import AppConfig
from django.db.models.signals import pre_save
from .signals import pre_save_receive


class SignalLearningConfig(AppConfig):
    name = 'signal_learning'

    def ready(self):
        # Login admin site please
        pre_save.connect(pre_save_receive, dispatch_uid='pre_save_receive')
