from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages

from datetime import datetime

from .models import Student, Contact



# Create your views here.
def index(request):
    # user = request.user
    # parameters = {
    #     'user': user,
    # }
    
    return render(request, "index.html")

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
        password = request.POST.get('password')
        
        print("got the data")
        
        user = auth.authenticate(request, username=username, password=password)
        
        print("authenticated")
        
        if user is not None:
            
            user = Student.objects.get(username=username)
            auth.login(request, user)
            print("Logged in")
            return redirect('index')
        
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    return render(request, 'login.html')

def signup(request):
        
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            
            if Student.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                
            else:
                user = Student.objects.create_user(username=username)
                user.set_password(password)
                
                user.save()
                messages.success(request, "Account created successfully. Login Again")
                return redirect('login')
        
        else:
            messages.info(request, 'Passwords do not match')
    return redirect('login')
        
def logout(request):
    auth.logout(request)
    return redirect('index')

def team(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "team.html",parameters)

def class_9th(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_9th.html",parameters)

def class_10th(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_10th.html",parameters)

def class_11th(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_11th.html",parameters)

def class_12th(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "class_12th.html",parameters)

def bsc(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "bsc.html",parameters)

def btech(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "btech.html",parameters)

def skill(request):
    user = request.user
    
    parameters = {
        'user': user,
    }
    return render(request, "skill.html",parameters)

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


