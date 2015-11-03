from django.shortcuts import render
from models import TemperatureHistory, TemperatureSchedule, TemperatureScheduleForm

module_name = __name__.split('.')[0]

def index_get(request):
    return render(request, 'temperature/index.html', {'temp_list' : TemperatureHistory.objects.all() })

def schedule_get(request):
    print __name__
    return render(request, 'common/schedule.html', {
            'schedule_list' : TemperatureSchedule.objects.all(),
            'add_view' : module_name + ':schedule_add',
            'edit_view' : module_name + ':schedule_edit',
            'delete_view' : module_name + ':schedule_delete',
            'schedule_form' : TemperatureScheduleForm()})

def schedule_add(request):
    pass

def schedule_edit(request):
    pass

def schedule_delete(request):
    pass
