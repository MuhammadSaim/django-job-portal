from django.shortcuts import render, redirect
from helpers.helpers import is_ajax
from django.http import JsonResponse
from validations.register_form import RegisterForm
from validations.login_form import LoginForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse


# login view for the user and submitting form will authenticate the user
def login_view(request):
    if request.user.is_authenticated:
        return redirect('public.home')
    if is_ajax(request) and request.method == 'POST':
        login_validate = LoginForm(request.POST)
        validation_status = login_validate.validate()
        if validation_status:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'error': False,
                    'form': False,
                    'redirect_url': reverse('auth.register'),
                    'messages': 'You are login successfully.'
                })
            else:
                return JsonResponse({
                    'error': True,
                    'form': False,
                    'messages': 'Invalid username or password'
                })
        else:
            return JsonResponse({
                'error': True,
                'form': True,
                'messages': login_validate.get_message_plain()
            })
    return render(request, 'public/auth/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('public.home')
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
                'messages': register_validate.get_message_plain()
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


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('auth.login')
    return redirect('public.home')
