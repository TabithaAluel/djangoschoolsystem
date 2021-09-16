from django.conf.urls import url
from . import views 
from .views import cal_profile, edit_cal


urlpatterns=[
 url('eventcalendar/',views.CalendarView.as_view(), name="calendar"),
 url('eventform/', views.event, name='eventform'),
 url("profile/<int:id>/", cal_profile, name="cal_profile"),
 url("edit/<int:id>/", edit_cal, name="edit_cal"),
     

] 
