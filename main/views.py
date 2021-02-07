from django.shortcuts import render, redirect
from menu.models import Order, Menu
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="Login_page")
def dashboard(request):
    return render(request, 'main/main.html', {'orders': Order.objects.all(), 
                                              'today_day': date.today().day,
                                              'menus': Menu.objects.all().order_by('day')})

def register(request):
    if request.user.is_authenticated:
        return redirect('Noras Dasboard')
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login_page')

    context = {'UserCreationForm' : form}
    return render(request, 'main/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('Noras Dasboard')
    if request.method == "POST":
        user = request.POST.get('username')
        passw = request.POST.get('password')

        user = authenticate(request, username=user, password=passw)
        if user is not None:
            login(request, user)
            return redirect('Noras Dasboard')
        else:
            messages.error(request, "User Or Password Incorrect")

    return render(request, 'main/login.html', {})

def logout_page(request):
    logout(request)
    return redirect('Login_page')