from django.shortcuts import render, redirect

class ScheduleViews:
    def __init__(self, module_name, model_class, modelform_class):
        self._module_name = module_name
        self._model_class = model_class
        self._modelform_class = modelform_class

    def get(self, request):
        return render(request, 'common/schedule.html', {
            'schedule_list' : self._model_class.objects.all(),
            'add_view' : self._module_name + ':schedule_add',
            'edit_view' : self._module_name + ':schedule_edit',
            'delete_view' : self._module_name + ':schedule_delete',
            'schedule_form' : self._modelform_class() })

    def add(self, request):
        if not request.POST:
            raise Exception(self._module_name + ".schedule_add not invoked with POST")
        task = self._modelform_class(request.POST)
        if not task.is_valid():
            raise Exception(self._module_name + ".shedule_add form validation fails")
        task.save()
        return redirect(self._module_name + ':schedule_get')

    def edit(self, request, id):
        task = self._model_class.objects.get(id = id)
        if not task:
            raise Exception("Cannot found task for edit")
        if not request.POST:
            return _schedule_edit_fill_form(request, task)
        else:
            return _schedule_edit_commit_changes(request, task)

    def _edit_fill_form(self, request, task):
        add_form = self._modelform_class(instance = task)
        return render(request, 'common/schedule.html', {
            'schedule_list' : self._model_class.objects.all(),
            'add_view' : self._module_name + ':schedule_add',
            'edit_view' : self._module_name + ':schedule_edit',
            'delete_view' : self._module_name + ':schedule_delete',
            'schedule_form' : add_form,
            'edited_id' : task.id })

    def _edit_commit_changes(self, request, task):
        changes = self._modelform_class(request.POST, instance = task)
        if not changes.is_valid():
            raise Exception(self._module_name + ".shedule_add form validation fails")
        changes.save()
        return redirect(self._module_name + ':schedule_get')

    def delete(self, request, id):
        task = self._model_class.objects.get(id = id)
        if not task:
            raise Exception("Cannot found task for delete")
        task.delete()
        return redirect(self._module_name + ':schedule_get')
