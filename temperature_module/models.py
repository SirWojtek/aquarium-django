from datetime import datetime
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

class TemperatureHistory:
    class TemperatureRecord:
        def __init__(self, dbus_record):
            self.value = dbus_record[0]
            self.timestamp = datetime(year = dbus_record[1], month = dbus_record[2],
                day = dbus_record[3], hour = dbus_record[4],
                minute = dbus_record[5], second = dbus_record[6])

    def __init__(self, dbus_history):
        self._history = [ TemperatureRecord(x) for x in dbus_history ]

    def __iter__(self):
        return self._history.__iter__()

    def next(self):
        return self._history.next()
