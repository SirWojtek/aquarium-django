from django.shortcuts import render

def index_get(request):
    return render(request, 'stat/index.html', {})
