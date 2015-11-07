from django.shortcuts import render
from models import Status

def index_get(request):
    status = Status.objects.all()

    temp_value = 'No data'
    heating_status = 'No data'
    filter_status = 'No data'
    light_status = 'No data'
    timestamp = 'No data'

    if status:
        temp_value = status[0].temperature
        heating_status = status[0].heating_status
        filter_status = status[0].filter_status
        light_status = status[0].light_status
        timestamp = status[0].last_update

    return render(request, 'stat/index.html', {
        'temp_value' : temp_value,
        'heating_status' : heating_status,
        'filter_status' : filter_status,
        'light_status' : light_status,
        'timestamp' : timestamp })
