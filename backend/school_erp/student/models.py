from django.db import models

# Create your models here.

class Student(models.Model) :
    teacher_id = models.CharField(max_length=10, default="")
    profile_img = models.FileField(upload_to='images/', default="")
    course = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    guardian_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    place = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=20)

    