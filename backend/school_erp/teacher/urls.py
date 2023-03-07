from django.urls import path
from . import views

urlpatterns = [
    path("login", views.teacherLog_fun, name="teacherLog"),
    path("add-teacher", views.addTeacher_fun, name="addTeacher_fun"),
    path('view_student/', views.view_student, name='view_student'),



#     path("student_registration",views.studentReg_fun, name="stdRegister"),
#     path("student_list",views.studentView_fun, name="student_list"),
#     path("attendance",views.attendance_fun, name="attendance"),
#     path("change_password",views.changePassword_fun, name="changePassword"),
#     path("profile",views.profile_fun, name="profile"),
#     path("add_exam",views.addExam_fun, name="addExam"),
#     path("delete_exam",views.deleteExam_fun, name="deleteExam"),
]
