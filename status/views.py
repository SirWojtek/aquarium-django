from django.shortcuts import render

def status_get(request):
    return render(request, 'status.html', {})
