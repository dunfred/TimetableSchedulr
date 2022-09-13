from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _


TIME_SLOTS = (
    ('6:30 am - 7:30 am',     '6:30 am - 7:30 am'),
    ('7:30 am - 8:30 am',     '7:30 am - 8:30 am'),
    ('8:30 am - 9:30 am',     '8:30 am - 9:30 am'),
    ('9:30 am - 10:30 am',    '9:30 am - 10:30 am'),
    ('10:30 am - 11:30 am',   '10:30 am - 11:30 am'),
    ('11:30 am - 12:30 pm',   '11:30 am - 12:30 pm'),
    ('12:30 pm - 1:30 pm',    '12:30 pm - 1:30 pm'),
    ('1:30 pm - 2:30 pm',     '1:30 pm - 2:30 pm'),
    ('2:30 pm - 3:30 pm',     '2:30 pm - 3:30 pm'),
    ('3:30 pm - 4:30 pm',     '3:30 pm - 4:30 pm'),
    ('4:30 pm - 5:30 pm',     '4:30 pm - 5:30 pm'),
    ('5:30 pm - 6:30 pm',     '5:30 pm - 6:30 pm'),
)

DAYS = (
    ('Monday',      'Monday'),
    ('Tuesday',     'Tuesday'),
    ('Wednesday',   'Wednesday'),
    ('Thursday',    'Thursday'),
    ('Friday',      'Friday'),
)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.name).title()

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    faculty         = models.ForeignKey(Faculty, related_name="departments")

    def __str__(self):
        return f"{self.faculty.faculty_name}: {self.department_name}".title()


class Programme(models.Model):
    programme_name   = models.CharField(max_length=100, unique=True, help_text="Ex: Information Technology (BSc) Level 100")
    department      = models.ForeignKey(Department, related_name="programmes")

    def __str__(self):
        return f"{self.department.department_name}: {self.programme_name}".title()


class Venue(models.Model):
    room = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.room).title()

class Course(models.Model):
    course_number = models.CharField(_("Course Number"), max_length=8, primary_key=True, help_text="Ex: INF101")
    course_name   = models.CharField(_("Course Name"), max_length=100)
    programme     = models.ForeignKey(Programme, related_name="courses")
    venue         = models.ForeignKey(Venue, related_name="courses")

    def __str__(self):
        return f'{self.course_number} {self.course_name}'


class Lecturer(models.Model):
    initials    = models.CharField(_("Initials"), max_length=6, help_text="Example: JD")
    full_name   = models.CharField(_("Full Name"), max_length=100, help_text="Example: John Doe")
    courses     = models.ManyToManyField(Course, null=True)
    department  = models.ForeignKey(Department, related_name="department_lecturers")

    def __str__(self):
        return f'{self.initials} {self.full_name}'


class Period(models.Model):
    course  = models.ForeignKey(Course, related_name="meeting_times")
    time    = models.CharField(_("Time"), max_length=15, choices=TIME_SLOTS, default='12:30 - 1:30')
    day     = models.CharField(_("Day"), max_length=10, choices=DAYS)

    def __str__(self):
        return f'{self.day} {self.time}'

    class Meta:
        unique_togetther = ('course', 'time', 'day',)
