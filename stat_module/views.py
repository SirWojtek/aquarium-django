from django.shortcuts import render
from models import Status, Settings
from dbus_communication.dbus_interface import Dbus

def index_get(request):
    status = Status(Dbus.get_temperature_status(), Dbus.get_manual_mode())
    settings = Settings(Dbus.get_temperature_settings())

    if not settings:
        raise Exception("No settings can be found")

    return render(request, 'stat/index.html', {
        'status' : status,
        'settings' : settings })
