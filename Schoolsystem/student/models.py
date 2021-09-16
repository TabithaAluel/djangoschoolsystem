from django.db import models
from django import forms

 
# Create your models here.
class Student(models.Model):
    def full_name(self):
         return f"{self.first_name}{self.last_name}"


    first_name=models.CharField(
    max_length=12, blank=True, null=True
    )
    last_name=models.CharField(
        max_length=12, blank=True, null=True
    )

    age = models.PositiveSmallIntegerField(blank=True, null=True)
    phone_number=models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    national_id= models.CharField(max_length= 20, blank=True, null=True)
    profile_pic=models.ImageField(upload_to='images/', blank=True, null=True)
    gender_choices=((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Other'))
    gender=models.CharField(max_length=1,choices=gender_choices, blank=True, null=True)
   
    guardian_name = models.CharField(
        max_length=12, blank=True, null=True
    )
    email_address= models.EmailField(blank=True, null=True)
    # country_choice=((u's',u'South Sudan'),(u'K',u'Kenya'),(u's',u'Sudan'),( u'u','Uganda',(u'r','Rwanda')))
    # counry=models.CharField(max_length=1,choices=country_choice)

    country=models.CharField(max_length=12, blank=True, null=True)
    medical_report = models.FileField(blank=True, null=True)
    date_of_enrollment = models.DateField(blank=True, null=True)
    laptop_number = models.CharField(
        max_length=10, blank=True, null=True
    )
    course_name=models.CharField(
        max_length=12, blank=True, null=True
    )
    grade=models.CharField(
        max_length=2, blank=True, null=True
    )
    language_choice=((u'E',u'English'),(u'K',u'Kiswahili'),(u'K',u'Kisudi'))
    language=models.CharField(max_length=3,choices= language_choice, blank=True, null=True)

