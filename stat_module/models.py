from django import forms

class SettingsForm(forms.Form):
    manual_mode = forms.BooleanField(required = False)
    temperature = forms.IntegerField(required = False)

    def disable_edit(self):
        self.fields['temperature'].widget.attrs['readonly'] = True

class Status():
    def __init__(self, temperature, manual_mode):
        self.manual_mode = bool(manual_mode)
        self.temperature = temperature
        self.heating_status = None
        self.filter_status = None
        self.light_status = None
        self.last_update = None

class Settings():
    def __init__(self, temperature, manual_mode):
        self.manual_mode = bool(manual_mode)
        self.temperature = temperature
        self.heating_status = None
        self.filter_status = None
        self.light_status = None
        self.last_update = None

    @staticmethod
    def from_form(form):
        return Settings(form.cleaned_data['temperature'], form.cleaned_data['manual_mode'])

    def to_form_initial(self):
        return {
            'manual_mode' : self.manual_mode,
            'temperature' : self.temperature }
