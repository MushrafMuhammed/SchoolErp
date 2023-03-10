from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Teacher

from teacher.serializer import AttendanceSerializer, CheckAttendanceSerializer, TeacherSerializer


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
        return JsonResponse({'successMessage': 'Attendance Marked successfully'})
    else:
        return JsonResponse({'errorMessage': 'Data validation failed !'})

@api_view(["POST"])
def checkAttendance_fun(request):
    params = request.data
    serialized_data = CheckAttendanceSerializer(data=params)
    if serialized_data.is_valid():
        
        return JsonResponse({'successMessage': 'ready to mark '})
    else:
        return JsonResponse({'errorMessage': 'Already Attendance Marked'})

@api_view(["POST"])
def teacherProfile_fun(request):
    new_teacher = Teacher.objects.filter(
        id=request.data['id']
    )
    serialized_data = TeacherSerializer(new_teacher, many=True)
    # print(serialized_data.data)
    return JsonResponse({"teacher": serialized_data.data})

@api_view(["PUT"])
def changePassword_fun(request):
    teacherData = request.data
    # print(teacherData)
    try:
        newTeacher = Teacher.objects.get(
            id=teacherData["teacherId"],
            password=teacherData["oldPassword"]
        )
        # print(teacher)
        newTeacher.password = teacherData["newPassword"]
        print(newTeacher.password)
        newTeacher.save()
        return JsonResponse({"msg": "valid"})
    except:
        return JsonResponse({"msg": "invalid"})