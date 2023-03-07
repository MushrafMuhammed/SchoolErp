from django.db import models

# Create your models here.

class Administrator(models.Model) :
    emp_id = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    designation = models.CharField(max_length=30)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)