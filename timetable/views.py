from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from timetable.models import Period

# Create your views here.

def index_view(request):
    context = {}
    template_name = "index.html"
    return render(request, template_name, context)

@login_required(login_url='user:login')
def dashboard_view(request):
    context = {}
    template_name = "dashboard.html"
    return render(request, template_name, context)


@login_required(login_url='user:login')
def timetable_view(request):
    context = {}
    template_name = "timetable.html"
    if request.user.is_authenticated:
        # Get all courses for current user(lecturer)
        periods = Period.objects.filter(
            course__course_code__in = list(request.user.courses.all().values_list('course_code', flat=True))
            )
        
        context["periods"] = periods

    return render(request, template_name, context)


@login_required(login_url='user:login')
def add_lecture_view(request):
    context = {}
    template_name = "add_lectures.html"
    return render(request, template_name, context)