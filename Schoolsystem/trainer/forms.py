from django import forms
from .models import Trainer
from django.db import models
from django.forms import fields


class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model= Trainer
        fields= "__all__" 
