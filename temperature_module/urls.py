from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index_get, name = 'index_get'),
    url(r'^schedule/', views.schedule_get, name = 'schedule_get'),
    url(r'^schedule/(\d+)/edit', views.schedule_get, name = 'schedule_edit'),
    url(r'^schedule/(\d+)/delete', views.schedule_get, name = 'schedule_detele'),
]
