from django.shortcuts import render
from models import TemperatureScheduleForm, TemperatureDbusInterface, TemperatureHistory
from schedule.views import ScheduleViews
from dbus_communication.dbus_interface import Dbus

schedule_views = ScheduleViews(__name__.split('.')[0],
    TemperatureDbusInterface(), TemperatureScheduleForm)

def index_get(request):
    history = TemperatureHistory(Dbus.get_temperature_history())
    return render(request, 'temperature/index.html', {'temp_list' : history })

def schedule_get(request):
    return schedule_views.get(request)

def schedule_add(request):
    return schedule_views.add(request)

def schedule_edit(request, id):
    return schedule_views.edit(request, id)

def schedule_delete(request, id):
    return schedule_views.delete(request, id)
