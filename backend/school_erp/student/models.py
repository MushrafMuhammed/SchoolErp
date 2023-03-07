from django.db import models

# Create your models here.

class Student(models.Model) :
    course = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    dob = models.CharField(max_length=25)
    guardian_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=40)
    place = models.CharField(max_length=30)
    pincode = models.CharField(max_length=6)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)