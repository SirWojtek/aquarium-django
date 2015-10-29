from django.shortcuts import render
from models import Temperature

def index_get(request):
    return render(request, 'temperature/index.html', {'temp_list' : Temperature.objects.all() })
