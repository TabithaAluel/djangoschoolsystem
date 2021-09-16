
from django.shortcuts import render
from .forms import CoursesForm
from .models import Courses
from django.shortcuts import redirect, render





# Create your views here.

def register_courses(request):
    form = CoursesForm()
    return render(request,"register_courses.html",{"form":form})

def register_courses(request):
    if request.method=="POST":
        form=CoursesForm(request.POST)
        if form.is_valid():
           form.save()
        else:
            print(form.errors)   
    else:
        form=CoursesForm()    
    return render(request, "register_courses.html", {"form":form})  

def course_list(request):   
    course=Courses.objects.all() 
    return render(request, "course_list.html",
    {"course":course})


def course_profile(request,id):
    courses=Courses.objects.get(id=id)
    return render(request,"course_profile.html",{'courses':courses})

def edit_course(request,id) :
    courses=Courses.objects.get(id=id)
    # form = None
    if request.method == "POST":
        form=CoursesForm(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect("course_profile", id=courses.id, )
    else:

            form=CoursesForm(instance=courses)
            return render(request, "edit_course.html", {"form" : form})
 
        







# Create your views here.
