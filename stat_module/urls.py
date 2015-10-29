from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.status_get, name = 'status_get'),
]
