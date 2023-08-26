from django.shortcuts import render
from helpers.helpers import is_ajax
from django.http import JsonResponse
from validations.register_form import RegisterForm
from django.contrib.auth import get_user_model


# Create your views here.
def login_view(request):
    return render(request, 'public/auth/login.html')


def register_view(request):
    return render(request, 'public/auth/register.html')


"""
A function is use to register the candidate to the system
"""


def register_candidate(request):
    if is_ajax(request) and request.method == 'POST':
        register_validate = RegisterForm(request.POST)
        validation_status = register_validate.validate()
        if validation_status:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = get_user_model()
            user = user.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            return JsonResponse({
                'error': False,
                'form': False,
                'messages': 'Candidate is created successfully.'
            })
        else:
            return JsonResponse({
                'error': True,
                'form': True,
                'messages': register_validate.get_message()
            })


"""
A function is use to register the employer to the system
"""


def register_employer(request):
    if is_ajax(request) and request.method == 'POST':
        register_validate = RegisterForm(request.POST)
        validation_status = register_validate.validate()
        if validation_status:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = get_user_model()
            user = user.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_company=True
            )
            return JsonResponse({
                'error': False,
                'form': False,
                'messages': 'Employer is registered successfully.'
            })
        else:
            return JsonResponse({
                'error': True,
                'form': True,
                'messages': register_validate.get_message()
            })
