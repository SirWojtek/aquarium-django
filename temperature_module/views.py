from django.shortcuts import render
from models import TemperatureHistory, TemperatureSchedule, TemperatureScheduleForm

def index_get(request):
    return render(request, 'temperature/index.html', {'temp_list' : TemperatureHistory.objects.all() })

def schedule_get(request):
    return render(request, 'common/schedule.html', {
            'schedule_list' : TemperatureSchedule.objects.all(),
            'edit_view' : 'schedule_edit',
            'delete_view' : 'schedule_delete',
            'schedule_form' : TemperatureScheduleForm()})

def schedule_edit(request):
    pass

def schedule_delete(request):
    pass
