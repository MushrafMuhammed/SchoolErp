from django.http import JsonResponse
from django.shortcuts import render
from student.models import Student

from student.serializer import StudentSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(["POST"])
def addStudent_fun(request):
    params = request.data
    serialized_data = StudentSerializer(data=params)
    print(serialized_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'successMessage': 'Data inserted successfully'})
    else:
        return JsonResponse({'errorMessage': 'Data validation failed !'})


@api_view(["POST"])
def studentLogin_fun(request):
    user_name = request.POST["username"]
    user_pass = request.POST["password"]

    try:
        student = Student.objects.get(
            email=user_name,
            password=user_pass
        )

        status = True
        return JsonResponse({"statusCode": status, "token": student.id})
    except:
        status = False
    return JsonResponse({"statusCode": status})


@api_view(["POST"])
def loadstudent_fun(request):
    new_student = Student.objects.filter(
        id=request.data['id']
    )
    serialized_data = StudentSerializer(new_student, many=True)
    # print(serialized_data.data)
    return JsonResponse({"student": serialized_data.data})


@api_view(["PUT"])
def changePassword_fun(request):
    studentData = request.data
    # print(studentData)
    try:
        newStudent = Student.objects.get(
            id=studentData["studentId"],
            password=studentData["oldPassword"]
        )
        # print(student)
        newStudent.password = studentData["newPassword"]
        print(newStudent.password)
        newStudent.save()
        return JsonResponse({"msg": "valid"})
    except:
        return JsonResponse({"msg": "invalid"})

@api_view(["GET"])
def viewStudent_fun(request):
    students = Student.objects.all()
    serializer_data = StudentSerializer(students,many = True)
    # print(serializer_data)
    return JsonResponse({"studentList":serializer_data.data})