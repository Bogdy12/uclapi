from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^personal$', views.get_personal_timetable),
    url(r'^bymodule$', views.get_modules_timetable),
]