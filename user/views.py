from django.contrib import auth #, messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
def login_view(request):
    context = {}
    template_name = "login.html"

    if request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)
        auth.login(request, user)

        # Check if user was attempting to visit another page
        url = request.META.get('HTTP_REFERER')
        try:
            query = requests.utils.urlparse(url).query
            params = dict(x.split('=') for x in query.split('&'))

            if 'next' in params:
                nextPage = params['next']
                return redirect(nextPage)
        except Exception:
            return redirect('timetable:dashboard')

    return render(request, template_name, context)


@login_required(login_url='user:login')
def logout_view(request):
    auth.logout(request)
    return redirect('user:login')


