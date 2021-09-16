from cal.models import Event
from django.shortcuts import render

# Create your views here.
from .serializers import StudentSerializer
from rest_framework import viewsets
from student.models import Student
from .serializers import TrainerSerializer
from trainer.models import Trainer
from courses.models import Courses
from .serializers import CourseSerializer
from .serializers import EventSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class = TrainerSerializer

    
class CoursesViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class = CourseSerializer

    
class EventViewSet(viewsets.ModelViewSet):
    queryset=Event.objects.all()
    serializer_class = EventSerializer

    

