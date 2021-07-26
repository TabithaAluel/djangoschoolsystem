from django.db import models
from django import forms
from django.db.models import manager
from django.db.models.enums import Choices
 
# Create your models here.
class Student(models.Model):
    first_name=models.CharField(
    max_length=12
    )
    last_name=models.CharField(
        max_length=12
    )
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    national_id= models.CharField(
        max_length= 20
    )
    gender_choices=((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Other'))
    gender=models.CharField(max_length=1,choices=gender_choices)
   
    guardian_name = models.CharField(
        max_length=12
    )
    email_address= models.EmailField()
    county = models.CharField(
        max_length=12
    )
   
    medical_report = models.FileField()
    date_of_enrollment = models.DateField()
    laptop_number = models.CharField(
        max_length=10
    )
    course_name=models.CharField(
        max_length=12
    )
    grade=models.CharField(
        max_length=2
    )
    Language_choice=((u'E',u'English'),(u'K',u'Kiswahili'),(u'K',u'Kisudi'))
    Language=models.CharField(max_length=3,choices= Language_choice)

