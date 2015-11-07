from django.shortcuts import render
from models import Status, Settings

def index_get(request):
    status = Status.get()
    settings = Settings.get()

    temp_value_status = 'No data'
    heating_status = 'No data'
    filter_status = 'No data'
    light_status = 'No data'
    status_timestamp = 'No data'

    if status:
        temp_value_status = status.temperature
        heating_status = status.heating_status
        filter_status = status.filter_status
        light_status = status.light_status
        status_timestamp = status.last_update

    return render(request, 'stat/index.html', {
        'temp_value_status' : temp_value_status,
        'heating_status' : heating_status,
        'filter_status' : filter_status,
        'light_status' : light_status,
        'status_timestamp' : status_timestamp,
        'temp_value_settings' : settings.temperature,
        'heating_settings' : settings.heating_status,
        'filter_settings' : settings.filter_status,
        'light_settings' : settings.light_status,
        'settings_timestamp' : settings.last_update })
