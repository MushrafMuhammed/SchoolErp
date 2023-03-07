from django.shortcuts import render

# Create your views here.

def profile_fun(request):
    return render(request, "profile.html")

def exam_fun(request):
    return render(request, "exams.html")

def changePassword_fun(request):
    return render(request, "change_password.html")

def updateProfile_fun(request):
    return render(request, "update_profile.html")

