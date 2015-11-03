from django.shortcuts import render, redirect
from models import TemperatureHistory, TemperatureSchedule, TemperatureScheduleForm

module_name = __name__.split('.')[0]

def index_get(request):
    return render(request, 'temperature/index.html', {'temp_list' : TemperatureHistory.objects.all() })

def schedule_get(request):
    return render(request, 'common/schedule.html', {
        'schedule_list' : TemperatureSchedule.objects.all(),
        'add_view' : module_name + ':schedule_add',
        'edit_view' : module_name + ':schedule_edit',
        'delete_view' : module_name + ':schedule_delete',
        'schedule_form' : TemperatureScheduleForm() })

def schedule_add(request):
    if not request.POST:
        raise Exception(module_name + ".schedule_add not invoked with POST")
    task = TemperatureScheduleForm(request.POST)
    if not task.is_valid():
        raise Exception(module_name + ".shedule_add form validation fails")
    task.save()
    return redirect(module_name + ':schedule_get')

def schedule_edit(request):
    pass

def schedule_delete(request):
    pass
