from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Lunch
from .forms import MealForm, SaladForm, DessertForm, LunchForm


def menu_hub(request):
    return render(request, 'menu/menu.html', {'lunchs': Lunch.objects.all()})

def create(request):

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
    return render(request, 'menu/create.html', forms)

def menus_day(requests, menu_uuid):
    return render(requests, 'menu/create.html')