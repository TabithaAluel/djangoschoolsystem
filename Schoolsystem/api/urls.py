from django.urls import path, include
from rest_framework import routers
from .views import EventViewSet, StudentViewSet
from .views import TrainerViewSet
from .views import CoursesViewSet



router=routers.DefaultRouter()
router.register (r"students", StudentViewSet)
router.register(r"trainers",TrainerViewSet )
router.register(r"courses",CoursesViewSet )
router.register(r"event",EventViewSet )

urlpatterns=[
    path("", include(router.urls)),

]