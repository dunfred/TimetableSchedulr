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

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        
    def __str__(self):
        return str(self.name).title()

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    faculty         = models.ForeignKey(Faculty, related_name="departments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty.faculty_name}: {self.department_name}".title()


class Programme(models.Model):
    programme_name   = models.CharField(max_length=100, unique=True, help_text="Ex: Information Technology (BSc) Level 100")
    department      = models.ForeignKey(Department, related_name="programmes", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.department.department_name}: {self.programme_name}".title()


class Venue(models.Model):
    room = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.room).title()

class Course(models.Model):
    course_number = models.CharField(_("Course Number"), max_length=8, primary_key=True, help_text="Ex: INF101")
    course_name   = models.CharField(_("Course Name"), max_length=100)
    programme     = models.ForeignKey(Programme, related_name="courses", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course_number} {self.course_name}'


class Period(models.Model):
    course  = models.ForeignKey(Course, related_name="meeting_times", on_delete=models.CASCADE)
    venue   = models.ForeignKey(Venue, related_name="periods", on_delete=models.CASCADE)
    time    = models.CharField(_("Time"), max_length=25, choices=TIME_SLOTS, default='08:30 am - 09:30 am')
    day     = models.CharField(_("Day"), max_length=10, choices=DAYS)

    def __str__(self):
        return f'{self.day} {self.time}'

    class Meta:
        unique_together = ('course', 'venue', 'time', 'day',)
