from django.db import models
from schedule.models import GenericSchedule
from django.forms import ModelForm

class FilterHistory(models.Model):
    status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True)

class FilterSchedule(GenericSchedule):
    status = models.BooleanField()

class FilterScheduleForm(ModelForm):
    class Meta:
        model = FilterSchedule
        fields = GenericSchedule.form_fields
