from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface, Task
from dbus_communication.dbus_interface import Dbus

class TemperatureScheduleForm(ScheduleForm):
    status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    def __init__(self):
        self._task_list = self._update_task_list()

    def get_schedule_list(self):
        return self._task_list

    def add_schedule_task(self, task):
        data = task.cleaned_data
        task = (
            data['start_day'], (data['start_time'].hour, data['start_time'].minute),
            data['end_day'], (data['end_time'].hour, data['end_time'].minute),
            data['status'])
        Dbus.add_schedule_task(task)

    def update_schedule_task(self, old_task, new_task):
        print "update"
        print old_task, new_task

    def remove_schedule_task(self, task):
        print "remove"
        print task

    def _update_task_list(self):
        current_id = 1
        task_list = []
        for task in Dbus.get_schedule_list():
            task_list.append(Task(current_id, task))
            current_id += 1
        return task_list
