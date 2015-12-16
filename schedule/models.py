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

# This is abstract form used for creating schedule for each module.
class ScheduleForm(forms.Form):
    start_time = forms.TimeField()
    start_day = forms.ChoiceField(choices = DAYS_OF_WEEK)
    end_time = forms.TimeField()
    end_day = forms.ChoiceField(choices = DAYS_OF_WEEK)
    status = None  # to be overriten in child forms

    def __repr__(self):
        return self._get_js_format()

    def _get_js_format(self):
        return """{ start_time : \'%s\',
            start_day : \'%s\',
            end_time : \'%s\',
            end_day : \'%s\' }""" % (self.start_time, self.start_day,
                self.end_time, self.end_day)

class Task:
    def __init__(self, id, dbus_task):
        self.id = id
        self.start_day = Task._get_readable_day(dbus_task[0])
        self.start_time = time(dbus_task[1][0], dbus_task[1][1])
        self.end_day = Task._get_readable_day(dbus_task[2])
        self.end_time = time(dbus_task[3][0], dbus_task[3][1])
        self.status = dbus_task[4]

    @staticmethod
    def _get_readable_day(raw_day):
        return next(x[1] for x in DAYS_OF_WEEK if x[0] == raw_day)

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
