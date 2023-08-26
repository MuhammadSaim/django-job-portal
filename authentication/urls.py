from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.login_view, name="auth.login"),
    path('register', views.register_view, name="auth.register"),
    path('register/candidate', views.register_candidate, name="auth.register.candidate"),
    path('register/employer', views.register_employer, name="auth.register.employer"),
]
