from django.db import models

class Temperature(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True)
