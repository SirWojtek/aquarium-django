from django.db import models
from schedule.models import GenericSchedule
from defaults import Default

class FilterHistory(models.Model):
    status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True)

    @staticmethod
    def get_current_filter_status():
        if FilterHistory.objects.count():
            return FilterHistory.objects.order_by('timestamp')[0]
        else:
            return None


class FilterSchedule(GenericSchedule):
    default_value = Default.filter_status
