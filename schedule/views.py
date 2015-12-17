from django.shortcuts import render, redirect
from models import Task

class ScheduleViews:
    def __init__(self, module_name, dbus_schedule_interface, form_class):
        self._module_name = module_name
        self._dbus_schedule_interface = dbus_schedule_interface
        self._form_class = form_class

    def get(self, request):
        return render(request, 'common/schedule.html', {
            'schedule_list' : self._dbus_schedule_interface.get_schedule_list(),
            'add_view' : self._module_name + ':schedule_add',
            'edit_view' : self._module_name + ':schedule_edit',
            'delete_view' : self._module_name + ':schedule_delete',
            'schedule_form' : self._form_class() })

    def add(self, request):
        if not request.POST:
            raise Exception(self._module_name + ".schedule_add not invoked with POST")
        task = self._form_class(request.POST)
        if not task.is_valid():
            raise Exception(self._module_name + ".shedule_add form validation fails")
        self._dbus_schedule_interface.add_schedule_task(Task.from_form(task))
        return redirect(self._module_name + ':schedule_get')

    def edit(self, request, id):
        if not request.POST:
            return self._edit_fill_form(request, id)
        else:
            return self._edit_commit_changes(request, id)

    def _edit_fill_form(self, request, id):
        task = self._dbus_schedule_interface.get_task_from_list(id)
        add_form = self._form_class(initial = task.to_form_initial())
        return render(request, 'common/schedule.html', {
            'schedule_list' : self._dbus_schedule_interface.get_schedule_list(),
            'add_view' : self._module_name + ':schedule_add',
            'edit_view' : self._module_name + ':schedule_edit',
            'delete_view' : self._module_name + ':schedule_delete',
            'schedule_form' : add_form,
            'edited_task' : task })

    def _edit_commit_changes(self, request, id):
        changes = self._form_class(request.POST)
        if not changes.is_valid():
            raise Exception(self._module_name + ".shedule_add form validation fails")
        self._dbus_schedule_interface.update_schedule_task(id, Task.from_form(changes))
        return redirect(self._module_name + ':schedule_get')

    def delete(self, request, task_id):
        self._dbus_schedule_interface.remove_schedule_task(task_id)
        return redirect(self._module_name + ':schedule_get')
