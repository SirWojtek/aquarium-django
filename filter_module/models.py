from django.db import models
from schedule.models import GenericSchedule
from defaults import Default

class FilterHistory(models.Model):
    status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True)

class FilterSchedule(GenericSchedule):
    default_value = Default.filter_status
