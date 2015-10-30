from django.db import models
from schedule.models import GenericSchedule
from defaults import Default

class TemperatureHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)

    @staticmethod
    def get_current_temperature():
        if TemperatureHistory.objects.count():
            return TemperatureHistory.objects.order_by('timestamp')[0]
        else:
            return None


class TemperatureSchedule(GenericSchedule):
    default_value = Default.temperature
