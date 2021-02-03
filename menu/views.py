from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Lunch, Menu
from .forms import MealForm, SaladForm, DessertForm, LunchForm, MenuForm


def menu_hub(request):
    return render(request, 'menu/menu.html', {'lunchs': Lunch.objects.all(), 'menus': Menu.objects.all()})

def create_lunch(request):

    # TODO send a popup message if fail or success
    if request.method == 'POST':
        form_filled = request.POST.dict()
        
        if "Meal" in form_filled.keys():
            form = MealForm(request.POST)

        if "Salad" in form_filled.keys():
            form = SaladForm(request.POST)

        if "Dessert" in form_filled.keys():
            form = DessertForm(request.POST)

        if "Lunch" in form_filled.keys():
            form = LunchForm(request.POST)
        
        if form.is_valid():
            form.save()

    forms = {'mealform'   : MealForm(), 
             'saladform'  : SaladForm(),
             'dessertform': DessertForm(),
             'lunchform'  : LunchForm() 
            }
    return render(request, 'menu/create_lunch.html', forms)

def create_menu(request):
    # TODO send a popup message if fail or success
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
    menu_form = {'menuform': MenuForm()}
    return render(request, 'menu/create_menu.html', menu_form) 


def menus_day(requests, menu_uuid):
    return render(requests, 'menu/menu.html')