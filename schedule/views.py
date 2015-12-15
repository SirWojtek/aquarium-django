from django.shortcuts import render, redirect

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
        self.dbus_schedule_interface.add_schedule_task(task)
        return redirect(self._module_name + ':schedule_get')

    def edit(self, request, task):
        if not request.POST:
            return _schedule_edit_fill_form(request, task)
        else:
            return _schedule_edit_commit_changes(request, task)

    def _edit_fill_form(self, request, task):
        add_form = self._form_class(instance = task)
        return render(request, 'common/schedule.html', {
            'schedule_list' : self._dbus_schedule_interface.get_schedule_list(),
            'add_view' : self._module_name + ':schedule_add',
            'edit_view' : self._module_name + ':schedule_edit',
            'delete_view' : self._module_name + ':schedule_delete',
            'schedule_form' : add_form,
            'edited_id' : task.id })

    def _edit_commit_changes(self, request, task):
        changes = self._form_class(request.POST)
        if not changes.is_valid():
            raise Exception(self._module_name + ".shedule_add form validation fails")
        self._dbus_schedule_interface.update_schedule_task(task, changes)
        return redirect(self._module_name + ':schedule_get')

    def delete(self, request, task):
        self.dbus_schedule_interface.remove_schedule_task(task)
        return redirect(self._module_name + ':schedule_get')
