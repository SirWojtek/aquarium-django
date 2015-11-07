from django.shortcuts import render
from models import Status, Settings

def index_get(request):
    status = Status.get()
    settings = Settings.get()

    if not settings:
        raise Exception("No settings can be found")

    return render(request, 'stat/index.html', {
        'status' : status,
        'settings' : settings })
