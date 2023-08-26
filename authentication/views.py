from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def login_view(request):
    return render(request, 'public/auth/login.html')


def register_view(request):
    return render(request, 'public/auth/register.html')


def job_lists(request):
    return render(request, 'public/jobs/list.html')
