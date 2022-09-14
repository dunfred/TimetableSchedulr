from django.urls import path
from timetable import views

app_name = "timetable"

urlpatterns = [
    path('', views.index, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('timetable/', views.timetable, name="timetable"),
]
