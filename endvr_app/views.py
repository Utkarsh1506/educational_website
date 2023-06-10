from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from datetime import datetime

from .models import  Contact



# Create your views here.
def index(request):
    user = request.user
    parameters = {
        'user': user,
    }
    
    return render(request, "index.html",parameters)

def about(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    
    return render(request, 'about.html', parameters)

def contact(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(email=email, message=message)
        contact.save()
        
        messages.info(request, 'Your message has been sent')
        
        return redirect('contact')
    
    
    return render(request, 'contact.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(username=username, password=passwd)
            
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username or Password is incorrect')
            
        
    else:
        messages.info(request, 'Logged in successfully')
    
    return render(request, 'login.html')

def signup(request):
        
    if request.method == 'POST':
        fname = request.POST.get('fname')
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        
        user = User.objects.filter(username=username) 
        
        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('login')
        
        user = User.objects.create_user(username=username)
        
        user.set_password(passwd)
        user.save()
        
        messages.info(request, 'Account created successfully')
        
        return redirect('login')
       
        
    return render(request, 'login.html')
    
        
def logout(request):
    auth.logout(request)
    return redirect('index')

def team(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "team.html",parameters)

@login_required(login_url='login')
def class_9(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_9.html",parameters)

@login_required(login_url='login')
def class_10(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_10.html",parameters)

@login_required(login_url='login')
def class_11(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_11.html",parameters)

@login_required(login_url='login')
def class_12(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_12.html",parameters)

@login_required(login_url='login')
def bsc(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "bsc.html",parameters)

@login_required(login_url='login')
def btech(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "btech.html",parameters)

@login_required(login_url='login')
def skill(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "skill.html",parameters)

@login_required(login_url='login')
def course_details(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "course_details.html",parameters)

@login_required(login_url='login')
def Physics(request):
    user = request.user
    parameters = {
        'user': user,
    }
    return render(request, "Physics.html",parameters)

def terms_and_conditions(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "terms_and_conditions.html",parameters)

def hall_of_fame(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "hall_of_fame.html",parameters)


