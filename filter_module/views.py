from django.shortcuts import render
from models import FilterHistory

def index_get(request):
    return render(request, 'filter/index.html', {'filter_status_list' : FilterHistory.objects.all() })
