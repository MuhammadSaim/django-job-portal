from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.login_view, name="auth.login"),
    path('register', views.register_view, name="auth.register"),
    path('jobs', views.job_lists, name="auth.register"),
]