from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface
from dbus_communication.dbus_interface import Dbus

class TemperatureScheduleForm(ScheduleForm):
    status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    @staticmethod
    def get_schedule_list():
        return Dbus.get_schedule_list()

    @staticmethod
    def add_schedule_task(task):
        data = task.cleaned_data
        task = (
            data['start_day'], (data['start_time'].hour, data['start_time'].minute),
            data['end_day'], (data['end_time'].hour, data['end_time'].minute),
            data['status'])
        Dbus.add_schedule_task(task)

    @staticmethod
    def update_schedule_task(old_task, new_task):
        print "update"
        print old_task, new_task

    @staticmethod
    def remove_schedule_task(task):
        print "remove"
        print task
