from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface

class FilterScheduleForm(ScheduleForm):
    status = forms.BooleanField()

class FilterDbusInterface(ScheduleDbusInterface):
    def __init__(self):
        ScheduleDbusInterface.__init__(self)

    def dbus_get_schedule_list(self):
    	return []
