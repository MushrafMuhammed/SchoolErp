from django.urls import path
from . import views

urlpatterns = [
    path("login", views.teacherLog_fun, name="teacherLog"),
    path("add-teacher", views.addTeacher_fun, name="addTeacher_fun"),
    # path('view_student/', views.view_student, name='view_student'),
    path("view-teacher",views.viewTeacher_fun, name="viewTeacher")
]
