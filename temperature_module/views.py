from django.shortcuts import render
from models import TemperatureHistory

def index_get(request):
    return render(request, 'temperature/index.html', {'temp_list' : TemperatureHistory.objects.all() })
