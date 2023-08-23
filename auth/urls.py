from django.urls import path
from auth import views

urlpatterns = [
    path('login', views.login_view, name="auth.login"),
    path('register', views.register_view, name="auth.register"),
]
