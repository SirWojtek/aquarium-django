from django.shortcuts import render, redirect
from models import Status, Settings, SettingsForm
from dbus_communication.dbus_interface import Dbus

def index_get(request):
    status = Status(Dbus.get_temperature_status(), Dbus.get_manual_mode())
    settings = Settings(Dbus.get_temperature_settings(), Dbus.get_manual_mode())

    return render(request, 'stat/index.html', {
        'status' : status,
        'settings' : settings })

def edit_settings(request):
    settings = Settings(Dbus.get_temperature_settings(), Dbus.get_manual_mode())
    if not request.POST:
        return _get_settings(request, settings)
    else:
        return _edit_settings(request, settings)

def _get_settings(request, settings):
    status = Status(Dbus.get_temperature_status(), Dbus.get_manual_mode())
    settings_form = SettingsForm(initial = settings.to_form_initial())

    if not settings.manual_mode:
        settings_form.disable_edit()

    return render(request, 'stat/edit_settings.html', {
        'settings_form' : settings_form,
        'editable' : settings.manual_mode })

def _edit_settings(request, settings):
    settings_form = SettingsForm(request.POST)
    if not settings_form.is_valid():
        raise Exception('SettingsForm validation fails')
    new_settings = Settings.from_form(settings_form)
    Dbus.set_manual_mode(new_settings.manual_mode)
    if new_settings.temperature != settings.temperature:
        Dbus.set_temperature_settings(new_settings.temperature)
    return redirect('stat_module:edit_settings')

