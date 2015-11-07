from django.db import models
from schedule.models import GenericSchedule
from django.forms import ModelForm
from defaults import Default

class TemperatureHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)

class TemperatureSchedule(GenericSchedule):
    default_value = Default.temperature

    status = models.IntegerField()

class TemperatureScheduleForm(ModelForm):
    class Meta:
        model = TemperatureSchedule
        fields = GenericSchedule.form_fields
