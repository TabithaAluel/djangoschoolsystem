from django.db import models
from django.db.models.fields import CharField, DurationField, TextField, TimeField
from django.db.models.fields.files import FileField
# from django.db.models.fields.related import ManyToManyField
# class   Students(models.Model):
#     name=CharField(max_length=20)

# def __str__(self):
#     return self.name    
   

class Courses(models.Model):
    name=CharField(max_length=12, blank=True, null=True)
    description=TextField(blank=True, null=True)
    course_duration=DurationField(blank=True, null=True)
    course_code=CharField(max_length=30, blank=True, null=True)
    schedule=FileField(blank=True, null=True )
    syllabus=TextField(blank=True, null=True )
    course_Time=TimeField(blank=True ,null=True )
    date_enrolled=models.DateField(blank=True, null=True)

    # Students=ManyToManyField(Students)
    

# def __str__(self):
#     return self.name   

# class Enrolment(models.Model)   :
#     Students=models.ForeignKey(Students, on_delete=models.CASCADE)  
#     Courses=models.ForeignKey(Courses, on_delete=models.CASCADE) 
#     date_enrolled=models.DateField()
# class Meta:
#     unique_together=[['Students', 'Courses']]  




    



   


# Create your models here.
