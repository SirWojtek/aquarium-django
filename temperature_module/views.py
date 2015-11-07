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

def schedule_edit(request, id):
    task = TemperatureSchedule.objects.get(id = id)
    if not task:
        raise Exception("Cannot found task for edit")
    if not request.POST:
        return _schedule_edit_fill_form(request, task)
    else:
        return _schedule_edit_commit_changes(request, task)

def _schedule_edit_fill_form(request, task):
    add_form = TemperatureScheduleForm(instance = task)
    return render(request, 'common/schedule.html', {
        'schedule_list' : TemperatureSchedule.objects.all(),
        'add_view' : module_name + ':schedule_add',
        'edit_view' : module_name + ':schedule_edit',
        'delete_view' : module_name + ':schedule_delete',
        'schedule_form' : add_form,
        'edited_id' : task.id })

def _schedule_edit_commit_changes(request, task):
    changes = TemperatureScheduleForm(request.POST, instance = task)
    if not changes.is_valid():
        raise Exception(module_name + ".shedule_add form validation fails")
    changes.save()
    return redirect(module_name + ':schedule_get')

def schedule_delete(request, id):
    task = TemperatureSchedule.objects.get(id = id)
    if not task:
        raise Exception("Cannot found task for delete")
    task.delete()
    return redirect(module_name + ':schedule_get')
