from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from courses.models import Course

# Create your views here.

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    user_courses = Course.objects.filter(quota_request__student=request.user)

    context = {'user_courses': user_courses}

    return render(request, 'students/home.html', context)

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'students/login.html', {
                'message': 'Invalid credentials.'
            })
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'students/login.html')