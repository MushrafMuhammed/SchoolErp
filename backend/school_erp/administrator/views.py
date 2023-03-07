from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from administrator.models import Administrator

# Create your views here.

# def home_fun(request):
#     return render(request,"home.html")

@api_view(["POST"])
def login_fun(request):
    username = request.POST['username']
    password = request.POST['password']
    
    try :
        newadmin =  Administrator.objects.get(
            username = username,
            password = password
        )
        status = True
    except : 
        status = False
    return JsonResponse({"statusCode": status})


    







































































    # name = request.POST["t_name "]
    # address = request.POST["t_address"] 
    # gender = request.POST["t_gender"] 
    # dob = request.POST["t_dob"]
    # pincode = request.POST["t_pincode"]
    # qualification = request.POST["t_qualifi"] 
    # phone = request.POST["t_phone"] 
    # email = request.POST["t_email "]

    # newteacher = Teacher(
    #     name = name,
    #     address = address,
    #     gender = gender,
    #     dob = dob,
    #     pincode = pincode,
    #     qualification = qualification,
    #     phone = phone,
    #     email = email
    # )


    # return 

# def teacherView_fu(request):
#     return render(request, "teacher_view.html")

# def studentView_fu(request):
#     return render(request, "student_view.html")



