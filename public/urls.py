from django.urls import path
from public import views

urlpatterns = [
    path('', views.home_view, name="public.home")
]