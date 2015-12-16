from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface, Task
from dbus_communication.dbus_interface import Dbus

class TemperatureScheduleForm(ScheduleForm):
    status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    def __init__(self):
        self._update_task_list()

    def get_schedule_list(self):
        self._update_task_list()
        return self._task_list

    def add_schedule_task(self, task):
        # print task.start_day
        Dbus.add_schedule_task(task.to_dbus_message())

    def update_schedule_task(self, old_task, new_task):
        print "update"
        print old_task, new_task

    def remove_schedule_task(self, id):
        to_remove = self._get_task_from_list(id)
        Dbus.remove_schedule_task(to_remove.to_dbus_message())

    def _update_task_list(self):
        current_id = 1
        self._task_list = []
        for task in Dbus.get_schedule_list():
            self._task_list.append(Task.from_dbus(current_id, task))
            current_id += 1

    def _get_task_from_list(self, id):
        id = int(id)
        return next(x for x in self._task_list if x.id == id)

    # @staticmethod
    # def _create_dbus_message_from_form(task):
    #     data = task.cleaned_data
    #     return ( data['start_day'], (data['start_time'].hour, data['start_time'].minute),
    #         data['end_day'], (data['end_time'].hour, data['end_time'].minute),
    #         data['status'])

    # @staticmethod
    # def _create_dbus_message_from_task(task_from_form):
    #     data = task_from_form.cleaned_data
    #     return ( data['start_day'], (data['start_time'].hour, data['start_time'].minute),
    #         data['end_day'], (data['end_time'].hour, data['end_time'].minute),
    #         data['status'])
