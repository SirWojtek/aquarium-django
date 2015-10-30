from django.shortcuts import render
from temperature_module.models import TemperatureHistory
from filter_module.models import FilterHistory

def index_get(request):
    temperature = TemperatureHistory.get_current_temperature()
    filter = FilterHistory.get_current_filter_status()

    temp_value = 'No data'
    temp_timestamp = 'No data'
    filter_status = 'No data'
    filter_timestamp = 'No data'

    if temperature:
        temp_value = temperature.value
        temp_timestamp = temperature.timestamp

    if filter:
        filter_status = filter.status
        filter_timestamp = filter.timestamp

    return render(request, 'stat/index.html', {
        'temp_value' : temp_value,
        'temp_timestamp' : temp_timestamp,
        'filter_status' : filter_status,
        'filter_timestamp' : filter_timestamp })
