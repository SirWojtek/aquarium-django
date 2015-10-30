"""aquarium_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from stat_module import urls as stat_module_urls
from temperature_module import urls as temperature_module_urls
from filter_module import urls as filter_module_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stat/', include(stat_module_urls, namespace = 'stat_module')),
    url(r'^temperature/', include(temperature_module_urls, namespace = 'temperature_module')),
    url(r'^filter/', include(filter_module_urls, namespace = 'filter_module')),
    url(r'^', include(stat_module_urls)),
]
