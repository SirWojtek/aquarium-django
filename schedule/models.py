from django.db import models



class GenericSchedule(models.Model):
    MONDAY = 'M'
    TUESDAY = 'TU'
    WEDNESDAY = 'W'
    THURSDAY = 'TH'
    FRIDAY = 'F'
    SATURDAY = 'SA'
    SUNDAY = 'SU'

    start_time = models.TimeField()
    end_time = models.TimeField()
