from django.db import models
from rest_framework import fields, serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
from cal.models import Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name",'last_name', "age","date_of_birth", "national_id", "profile_pic","gender","guardian_name", "email_address", "country", "medical_report","date_of_enrollment","laptop_number",
        "course_name", "grade","language")

class TrainerSerializer(serializers.ModelSerializer)   : 
    class Meta:
        model=Trainer  
        fields= ('first_name',
    'last_name',
    'age',
    'date_of_birth',
    'gender_choices',
    'gender',
    'bio',
    'Courses',
    'email_Address',
    'phone_number',
    'salary',
    'profile',
    'contract',
    'date_hired')
class CourseSerializer(serializers.ModelSerializer)   : 
    class Meta:
        model=Courses
        fields=(
    'course_duration',
   'course_code',
    'schedule',
    'syllabus',
    'course_Time',
    'date_enrolled',
   )
class EventSerializer(serializers.ModelSerializer)   : 
    class Meta:
        model=Event
        fields=(
           'title',
    'description',
    'start_time',
    'end_time')  