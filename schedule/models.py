from django import forms
from datetime import time


MONDAY = 'M'
TUESDAY = 'TU'
WEDNESDAY = 'W'
THURSDAY = 'TH'
FRIDAY = 'F'
SATURDAY = 'SA'
SUNDAY = 'SU'

DAYS_OF_WEEK = (
    (MONDAY, 'Monday'),
    (TUESDAY, 'Tuesday'),
    (WEDNESDAY, 'Wednesday'),
    (THURSDAY, 'Thursday'),
    (FRIDAY, 'Friday'),
    (SATURDAY, 'Saturday'),
    (SUNDAY, 'Sunday'))

def get_readable_day(raw_day):
    return next(x[1] for x in DAYS_OF_WEEK if x[0] == raw_day)

def get_raw_day(readable_day):
    return next(x[0] for x in DAYS_OF_WEEK if x[1] == readable_day)

# This is abstract form used for creating schedule for each module.
class ScheduleForm(forms.Form):
    start_time = forms.TimeField()
    start_day = forms.ChoiceField(choices = DAYS_OF_WEEK)
    end_time = forms.TimeField()
    end_day = forms.ChoiceField(choices = DAYS_OF_WEEK)
    status = None  # to be overriten in child forms

class Task:
    def __init__(self):
        self.id = 0
        self.start_day = None
        self.start_time = None
        self.end_day = None
        self.end_time = None
        self.status = None

    @staticmethod
    def from_dbus(id, dbus_task):
        task = Task()
        task.start_day = get_readable_day(dbus_task[0])
        task.start_time = time(dbus_task[1][0], dbus_task[1][1])
        task.end_day = get_readable_day(dbus_task[2])
        task.end_time = time(dbus_task[3][0], dbus_task[3][1])
        task.status = dbus_task[4]
        task.id = id
        return task

    @staticmethod
    def from_form(form_task):
        task = Task()
        task.start_day = get_readable_day(form_task.cleaned_data['start_day'])
        task.start_time = form_task.cleaned_data['start_time']
        task.end_day = get_readable_day(form_task.cleaned_data['end_day'])
        task.end_time = form_task.cleaned_data['end_time']
        task.status = form_task.cleaned_data['status']
        return task

    def to_dbus_message(self):
        return ( get_raw_day(self.start_day), (self.start_time.hour, self.start_time.minute),
            get_raw_day(self.end_day), (self.end_time.hour, self.end_time.minute),
            self.status)

    def to_form_initial(self):
        return {
            'start_day' : get_raw_day(self.start_day),
            'start_time' : self.start_time,
            'end_day' : get_raw_day(self.end_day),
            'end_time' : self.end_time,
            'status' : self.status }

    def __repr__(self):
        return self._get_js_format()

    def _get_js_format(self):
        return """{ start_time : \'%s\',
            start_day : \'%s\',
            end_time : \'%s\',
            end_day : \'%s\',
            id : \'%s\' }""" % (self.start_time, get_raw_day(self.start_day),
                self.end_time, get_raw_day(self.end_day), self.id)

class ScheduleDbusInterface:
    def __init__(self):
        self._update_task_list()

    def _update_task_list(self):
        current_id = 1
        self._task_list = []
        for task in self.dbus_get_schedule_list():
            self._task_list.append(Task.from_dbus(current_id, task))
            current_id += 1

    def get_task_from_list(self, id):
        id = int(id)
        return next(x for x in self._task_list if x.id == id)

    def get_schedule_list(self):
        self._update_task_list()
        return self._task_list

    def add_schedule_task(self, task):
        self.dbus_add_schedule_task(task.to_dbus_message())

    def update_schedule_task(self, old_task_id, new_task):
        old_task = self.get_task_from_list(old_task_id)
        self.dbus_update_schedule_task(old_task.to_dbus_message(), new_task.to_dbus_message())

    def remove_schedule_task(self, id):
        to_remove = self.get_task_from_list(id)
        self.dbus_remove_schedule_task(to_remove.to_dbus_message())

    def dbus_get_schedule_list(self):
        raise NotImplementedError()

    def dbus_add_schedule_task(self, task):
        raise NotImplementedError()

    def dbus_update_schedule_task(self, old_task, new_task):
        raise NotImplementedError()

    def dbus_remove_schedule_task(self, task):
        raise NotImplementedError()
