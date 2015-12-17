from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface, Task
from dbus_communication.dbus_interface import Dbus

class TemperatureScheduleForm(ScheduleForm):
    status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    def __init__(self):
        ScheduleDbusInterface.__init__(self)

    def dbus_get_schedule_list(self):
        return Dbus.get_schedule_list()

    def dbus_add_schedule_task(self, task):
        Dbus.add_schedule_task(task)

    def dbus_update_schedule_task(self, old_task, new_task):
        Dbus.update_schedule_task(old_task, new_task)

    def dbus_remove_schedule_task(self, task):
        Dbus.remove_schedule_task(task)
