from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index_get, name = 'index_get'),
]
