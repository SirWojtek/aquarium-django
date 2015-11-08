from django.db import models

# This is abstract model used for creating schedule tables for each module.
class GenericSchedule(models.Model):
    MONDAY = 'M'
    TUESDAY = 'TU'
    WEDNESDAY = 'W'
    THURSDAY = 'TH'
    FRIDAY = 'F'
    SATURDAY = 'SA'
    SUNDAY = 'SU'

    DAYS_OF_WEEK = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'))

    start_time = models.TimeField()
    start_day = models.CharField(max_length = 2, choices = DAYS_OF_WEEK)
    end_time = models.TimeField()
    end_day = models.CharField(max_length = 2, choices = DAYS_OF_WEEK)
    status = None  # to be overriten in child models

    form_fields = [ 'start_day', 'start_time', 'end_day', 'end_time', 'status' ]

    class Meta:
        abstract = True

    def __repr__(self):
        return self._get_js_format()

    def _get_js_format(self):
        return """{ start_time : \'%s\',
            start_day : \'%s\',
            end_time : \'%s\',
            end_day : \'%s\' }""" % (self.start_time, self.start_day,
                self.end_time, self.end_day)
