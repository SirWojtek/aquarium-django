from django.db import models
from schedule.models import GenericSchedule
from defaults import Default

class TemperatureHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def get_current_temperature(self):
        if len(self.objects):
            return self.objects.order_by('timestamp')[0].value
        else:
            return None


class TemperatureSchedule(GenericSchedule):
    default_value = Default.temperature
