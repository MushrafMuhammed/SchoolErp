from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Teacher

from teacher.serializer import TeacherSerializer


# Create your views here.

@api_view(["POST"])
def teacherLog_fun(request):
    username = request.POST["username"]
    password = request.POST["password"]

    try:
        newTeacher = Teacher.objects.get(
            email = username,
            password = password
        )
        status = True
         # store username in session
        request.session['teacherId'] = newTeacher.id
    except:
        status = False
    return JsonResponse({"statusCode": status})

def view_student(request):
    # Retrieve the user's details from the session
    teacher_id = request.session.get('teacherId', None)
    if teacher_id:
        teacher = Teacher.objects.get(id=teacher_id)
        # Pass the user's details to the template
        return render(request, 'view_student.html', {'teacher': teacher})
    else:
        # If the user is not logged in, redirect to the login page
        return redirect('/teacher/login')


@api_view(["POST"])
def addTeacher_fun(request):

    params = request.data
    serialized_data = TeacherSerializer(data=params)
    print(serialized_data)
    if serialized_data.is_valid():
        serialized_data.save()
        return JsonResponse({'errorMessage': 'Data inserted successfully'})
    else:
        return JsonResponse({'errorMessage': 'Data validation failed !'})

# @api_view(["POST"])
# def teacherLogin(request):


# def studentReg_fun(request):
#     return render(request, "student_register.html")

# def studentView_fun(request):
#     return render(request, "view_student.html")

# def attendance_fun(request):
#     return render(request, "attendance.html")

# def changePassword_fun(request):
#     return render(request, "change_password.html")

# def profile_fun(request):
#     return render(request, "profile.html")

# def addExam_fun(request):
#     return render(request, "add_exam.html")

# def deleteExam_fun(request):
#     return render(request, "delete_exam.html")
