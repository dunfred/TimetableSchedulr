from django.urls import path
from timetable import views

app_name = "timetable"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('timetable/', views.timetable_view, name="timetable"),
    path('add_lecture/', views.add_lecture_view, name="add_lecture"),
]
