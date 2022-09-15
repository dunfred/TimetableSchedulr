from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from timetable.models import Course, Period, Venue

# Create your views here.

def index_view(request):
    context = {}
    template_name = "index.html"
    return render(request, template_name, context)

@login_required(login_url='user:login')
def dashboard_view(request):
    context = {}
    template_name = "dashboard.html"
    if request.user.is_authenticated:
        # Get all courses for current user(lecturer)
        
        lecturer_periods = Period.objects.filter(
            course__course_code__in = list(request.user.courses.all().values_list('course_code', flat=True))
            )       
        monday      = lecturer_periods.filter(day__iexact='monday')
        tuesday     = lecturer_periods.filter(day__iexact='tuesday')
        wednesday   = lecturer_periods.filter(day__iexact='wednesday')
        thursday    = lecturer_periods.filter(day__iexact='thursday')
        friday      = lecturer_periods.filter(day__iexact='friday')

        context["monday"]    = monday
        context["tuesday"]   = tuesday
        context["wednesday"] = wednesday
        context["thursday"]  = thursday
        context["friday"]    = friday

    return render(request, template_name, context)


@login_required(login_url='user:login')
def timetable_view(request):
    context = {}
    template_name = "timetable.html"
    return render(request, template_name, context)


@login_required(login_url='user:login')
def add_lecture_view(request):
    context = {}
    template_name = "add_lectures.html"
    if request.user.is_authenticated:
        # Get all courses for current user(lecturer)
        lecturer_periods = Period.objects.filter(
            course__course_code__in = list(request.user.courses.all().values_list('course_code', flat=True))
            )       
        monday      = lecturer_periods.filter(day__iexact='monday')
        tuesday     = lecturer_periods.filter(day__iexact='tuesday')
        wednesday   = lecturer_periods.filter(day__iexact='wednesday')
        thursday    = lecturer_periods.filter(day__iexact='thursday')
        friday      = lecturer_periods.filter(day__iexact='friday')
        courses     = request.user.courses.all()
        taken_venues = list(Period.objects.all().values_list('venue', flat=True))
        free_venues = Venue.objects.exclude(id__in=taken_venues)

        context["monday"]    = monday
        context["tuesday"]   = tuesday
        context["wednesday"] = wednesday
        context["thursday"]  = thursday
        context["friday"]    = friday
        context["courses"]   = courses
        context["free_venues"]   = free_venues

    return render(request, template_name, context)

@login_required(login_url='user:login')
def create_period_view(request):
    if request.method == "POST":
        course_id  = request.POST.get('course', None)
        venue_id   = request.POST.get('venue', None)
        time    = request.POST.get('timings', None)
        day     = request.POST.get('days', None)

        course = Course.objects.filter(course_code=course_id).first()
        venue = Venue.objects.filter(id=venue_id).first()

        obj = Period.objects.create(
            course = course,
            venue = venue,
            time = time,
            day = day
        )

        # print(obj)

    return redirect('timetable:dashboard')
