from django import forms
from schedule.models import ScheduleForm, ScheduleDbusInterface

class TemperatureScheduleForm(ScheduleForm):
	status = forms.IntegerField()

class TemperatureDbusInterface(ScheduleDbusInterface):
    def get_schedule_list():
        pass

    def add_schedule_task(task):
        pass

    def update_schedule_task(old_task, new_task):
        pass

    def remove_schedule_task(task):
        pass
