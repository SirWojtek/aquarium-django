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
        print task
        return task

    def to_dbus_message(self):
        return ( get_raw_day(self.start_day), (self.start_time.hour, self.start_time.minute),
            get_raw_day(self.end_day), (self.end_time.hour, self.end_time.minute),
            self.status)

    def __repr__(self):
        return self._get_js_format()

    def _get_js_format(self):
        return """{ start_time : \'%s\',
            start_day : \'%s\',
            end_time : \'%s\',
            end_day : \'%s\' }""" % (self.start_time, get_raw_day(self.start_day),
                self.end_time, get_raw_day(self.end_day))

class ScheduleDbusInterface:
    @staticmethod
    def get_schedule_list():
        raise NotImplementedError()

    @staticmethod
    def add_schedule_task(task):
        raise NotImplementedError()

    @staticmethod
    def update_schedule_task(old_task, new_task):
        raise NotImplementedError()

    @staticmethod
    def remove_schedule_task(task):
        raise NotImplementedError()
