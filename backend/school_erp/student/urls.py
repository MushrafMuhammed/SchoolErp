from django.urls import path
from . import views

urlpatterns = [
    path("profile",views.profile_fun, name="profile"),
    path("exam",views.exam_fun, name="exam"),
    path("change_password",views.changePassword_fun, name="changePassword"),
    path("update_profile",views.updateProfile_fun, name="updateProfile"),    
]