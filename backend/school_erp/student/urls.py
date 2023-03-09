from django.urls import path
from . import views

urlpatterns = [
    path("addStudent", views.addStudent_fun, name="addStudent"),
    path("login", views.studentLogin_fun, name="studentLogin"),
    path("loadStudent", views.loadstudent_fun, name="loadstudent"),
    path("changePassword", views.changePassword_fun, name="changePassword"),
    path("view-student", views.viewStudent_fun, name="viewStudent"),
    path("my-students", views.viewMyStudent_fun, name="viewMyStudent"),
]
