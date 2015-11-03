from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index_get, name = 'index_get'),
    url(r'^schedule/', views.schedule_get, name = 'schedule_get'),
    url(r'^schedule/add', views.schedule_add, name = 'schedule_add'),
    url(r'^schedule/(\d+)/edit', views.schedule_edit, name = 'schedule_edit'),
    url(r'^schedule/(\d+)/delete', views.schedule_delete, name = 'schedule_detele'),
]
