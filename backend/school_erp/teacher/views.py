from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Teacher

from teacher.serializer import AttendanceSerializer, TeacherSerializer


# Create your views here.

@api_view(["POST"])
def teacherLog_fun(request):
    username = request.POST["username"]
    password = request.POST["password"]

    try:
        newTeacher = Teacher.objects.get(
            email=username,
            password=password
        )
        status = True
        teacherId = newTeacher.id
        return JsonResponse({"statusCode": status, "teacher_id": teacherId})

    except:
        status = False
    return JsonResponse({"statusCode": status})


@api_view(["POST"])
def addTeacher_fun(request):
    params = request.data
    serialized_data = TeacherSerializer(data=params)
    print(serialized_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'successMessage': 'Data inserted successfully'})
    else:
        return JsonResponse({'errorMessage': 'Data validation failed !'})


@api_view(["GET"])
def viewTeacher_fun(request):
    teachers = Teacher.objects.all()
    serialized_data = TeacherSerializer(teachers, many=True)
    print(serialized_data.data)
    return JsonResponse({"teachersList": serialized_data.data})


@api_view(["POST"])
def addAttendance_fun(request):
    params = request.data
    serialized_data = AttendanceSerializer(data=params)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'successMessage': 'Data inserted successfully'})
    else:
        return JsonResponse({'errorMessage': 'Data validation failed !'})
