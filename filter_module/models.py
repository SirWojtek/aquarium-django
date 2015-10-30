from django.db import models
from schedule.models import GenericSchedule
from defaults import Default

class FilterHistory(models.Model):
    status = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add = True)

    def get_current_filter_status(self):
        if len(self.objects):
            return self.objects.order_by('timestamp')[0].status
        else:
            return None


class FilterSchedule(GenericSchedule):
    default_value = Default.filter_status
