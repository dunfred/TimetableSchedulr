from django.contrib import admin
from timetable.models import *

# Register your models here.

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    search_fields = ['faculty_name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['department_name']
    autocomplete_fields = ['faculty']
    list_display = ['department_name','faculty']

@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    search_fields = ['programme_name']
    autocomplete_fields = ['department']
    list_display = ['programme_name','department']

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    search_fields = ['room']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['course_code','course_name']
    autocomplete_fields = ['programme']
    list_display = ['course_code','course_name','programme']

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    autocomplete_fields = ['course','venue']
    list_display = ['course','venue','time','day','changed']

    

