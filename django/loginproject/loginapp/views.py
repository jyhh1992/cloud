from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def open(request):
    return render(request, 'loginproject/open.html')

def signup(request):
    if request.method == "POST":

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            
            auth.login(request, user)

            return redirect('home')

    return render(request, "loginproject/signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, "loginproject/login.html",)
    else:
        return render(request, "loginproject/login.html")


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'loginproject/login.html')
    
def home(request):
    return render(request, 'loginproject/home.html')
    

def tuto(request):
    return render(request, 'loginproject/tuto.html')

def game(request):
    return render(request, 'loginproject/game.html')
    
def record(request):
    return render(request, 'loginproject/record.html')