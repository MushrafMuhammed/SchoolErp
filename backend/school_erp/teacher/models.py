from django.db import models

from student.models import Student

# Create your models here.

class Teacher(models.Model) :
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.CharField(max_length=50, default= "")
    pincode = models.CharField(max_length=25)
    qualification = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=20)

class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=15)
    mark = models.CharField(max_length=15)


class Exams(models.Model):
    exam_name = models.CharField(max_length=50)
    date = models.DateField()
    remark = models.CharField(max_length=100)

