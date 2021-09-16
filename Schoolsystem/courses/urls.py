from django.urls import path
from .views import register_courses
from .views import course_list
from .views import course_profile, edit_course



urlpatterns=[path("register/",register_courses, name="register_courses"),
 path("list/",course_list, name="course_list"),
 path("profile/<int:id>/", course_profile, name="course_profile"),
 path("edit/<int:id>/", edit_course, name="edit_course"),
             
] 
