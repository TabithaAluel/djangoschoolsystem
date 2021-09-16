from courses.models import Courses
from trainer.models import Trainer
from student.models import Student
from django.urls.conf import path
from.views import home
urlpatterns=[
path("",home, name="home_view"),


]

            