
from django.contrib import admin
from django.db import models


# Create your models here.
class Trainer(models.Model):
    def full_name(self):
         return f"{self.first_name}{self.last_name}"

    first_name=models.CharField(max_length=20, blank=True, null=True)
    last_name=models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender_choices=((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Other'))
    gender=models.CharField(max_length=1,choices=gender_choices,null=True,blank=True)
    bio=models.CharField(max_length=200, blank=True, null=True)
    Courses=models.CharField(max_length=30, blank=True, null=True)
    email_Address=models.EmailField(blank=True, null=True)
    phone_number=models.CharField(max_length=20,blank=True, null=True )
    salary=models.PositiveBigIntegerField(blank=True, null=True)
    profile=models.ImageField(upload_to="images/",blank=True, null=True)
    contract=models.FileField(blank=True, null=True)
    date_hired=models.DateField(blank=True, null=True)



    

   



