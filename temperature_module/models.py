from django.db import models

class TemperatureHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)
