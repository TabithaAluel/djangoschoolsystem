from django import forms
from django.db import models
from django.forms import fields
from django.forms.widgets import Textarea
from .models import Courses

class CoursesForm(forms.ModelForm):
    class Meta:

        model= Courses
        fields= "__all__" 
        widgets = {
      
      'description':Textarea(attrs={'class':'form_control','id':'des'}),
      'syllabus':Textarea(attrs={'class':'form_control','id':'des'})
    }

