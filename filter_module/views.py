from django.shortcuts import render
from models import FilterScheduleForm, FilterDbusInterface
from schedule.views import ScheduleViews

schedule_views = ScheduleViews(__name__.split('.')[0],
	FilterDbusInterface(), FilterScheduleForm)

def index_get(request):
    return render(request, 'filter/index.html', {'filter_status_list' : None })

def schedule_get(request):
    return schedule_views.get(request)

def schedule_add(request):
    return schedule_views.add(request)

def schedule_edit(request, id):
    return schedule_views.edit(request, id)

def schedule_delete(request, id):
    return schedule_views.delete(request, id)
