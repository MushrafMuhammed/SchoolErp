from django.urls import path
from . import views

urlpatterns = [
    path("login", views.teacherLog_fun, name="teacherLog"),
    path("add-teacher", views.addTeacher_fun, name="addTeacher_fun"),
    path("view-teacher",views.viewTeacher_fun, name="viewTeacher"),
    path('add-attendance', views.addAttendance_fun, name='addAttendance'),

]
