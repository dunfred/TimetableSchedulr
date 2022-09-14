from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {}
    template_name = "index.html"
    return render(request, template_name, context)

@login_required(login_url='user:login')
def dashboard(request):
    context = {}
    template_name = "dashboard.html"
    return render(request, template_name, context)

@login_required(login_url='user:login')
def timetable(request):
    context = {}
    template_name = "timetable.html"
    return render(request, template_name, context)


@login_required(login_url='user:login')
def add_lecture(request):
    context = {}
    template_name = "add_lectures.html"
    return render(request, template_name, context)