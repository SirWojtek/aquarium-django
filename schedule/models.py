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

    class Meta:
        abstract = True
