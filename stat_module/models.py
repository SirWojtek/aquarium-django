from django.db import models
from defaults import Default

# Contains data from driver
class Status(models.Model):
    temperature = models.IntegerField()
    heating_status = models.BooleanField()
    filter_status = models.BooleanField()
    light_status = models.BooleanField()
    last_update = models.DateTimeField(auto_now_add = True)

    # There should be only one record in this table
    def save(self, *args, **kwargs):
        Status.objects.all().delete()
        models.Model.save(self, *args, **kwargs)

# Contains data for driver
class Settings(models.Model):
    temperature = models.IntegerField()
    heating_status = models.BooleanField()
    filter_status = models.BooleanField()
    light_status = models.BooleanField()
    last_update = models.DateTimeField(auto_now_add = True)

    # There should be only one record in this table
    def save(self, *args, **kwargs):
        Settings.objects.all().delete()
        models.Model.save(self, *args, **kwargs)
