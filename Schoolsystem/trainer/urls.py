from .views import register_trainer
from .views import trainer_list
from .views import edit_trainer
from .views import trainer_profile                                                 


from django.urls import path
urlpatterns=[path("register/", register_trainer, name="register_trainer"),
  path("list/",trainer_list, name="trainer_list"),
  path("profile/<int:id>/", trainer_profile, name="trainer_profile"),
  path("edit/<int:id>/", edit_trainer, name="edit_trainer"),
             
]


