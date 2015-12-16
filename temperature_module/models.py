from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface

class TemperatureScheduleForm(ScheduleForm):
	status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    @staticmethod
    def get_schedule_list():
        pass

    @staticmethod
    def add_schedule_task(task):
        print task

    @staticmethod
    def update_schedule_task(old_task, new_task):
        print old_task, new_task

    @staticmethod
    def remove_schedule_task(task):
        print task
