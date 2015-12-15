from django.shortcuts import render
from models import Status, Settings
from dbus_communication.dbus_interface import Dbus

def index_get(request):
    status = _get_status()
    settings = Settings.get()

    if not settings:
        raise Exception("No settings can be found")

    return render(request, 'stat/index.html', {
        'status' : status,
        'settings' : settings })

def _get_status():
    status = Status()
    status.temperature = Dbus.get_temperature_status()
    return status
