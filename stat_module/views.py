from django.shortcuts import render
from models import Temperature

def status_get(request):
    return render(request, 'status.html', {'temp_list' : Temperature.objects.all() })
