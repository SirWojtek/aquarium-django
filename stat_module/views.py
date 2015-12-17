from django.shortcuts import render
from models import Status, Settings, SettingsForm
from dbus_communication.dbus_interface import Dbus

def index_get(request):
    status = Status(Dbus.get_temperature_status(), Dbus.get_manual_mode())
    settings = Settings(Dbus.get_temperature_settings(), Dbus.get_manual_mode())

    return render(request, 'stat/index.html', {
        'status' : status,
        'settings' : settings })

def edit_settings(request):
    if not request.POST:
        return _get_settings(request)
    else:
        return _edit_settings(request)

def _get_settings(request):
    status = Status(Dbus.get_temperature_status(), Dbus.get_manual_mode())
    settings = Settings(Dbus.get_temperature_settings(), Dbus.get_manual_mode())
    settings_form = SettingsForm(initial = settings.to_form_initial())

    if not settings.manual_mode:
        settings_form.disable_edit()

    return render(request, 'stat/edit_settings.html', {
        'settings_form' : settings_form,
        'editable' : settings.manual_mode })

def _edit_settings(request):
    pass
