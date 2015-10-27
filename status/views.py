from django.shortcuts import render, HttpResponse

def status_get(request):
    return HttpResponse("Hello World!")
