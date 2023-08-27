from django.shortcuts import render


# view for the application public page
def home_view(request):
    return render(request, 'public/home.html')
