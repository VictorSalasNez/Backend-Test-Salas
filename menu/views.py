from django.shortcuts import render, redirect
from django.http import HttpResponse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import datetime
# Create your views here.
from .models import Lunch, Menu, Order, Meal, Salad, Dessert
from .forms import MealForm, SaladForm, DessertForm, LunchForm, MenuForm, SelectMenuForm
from employees.models import Employee

os.environ['SLACK_BOT_TOKEN'] = "xoxb-1691797685303-1708676997845-jtGFddMOhEDsscCcjMqRUfw9"
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])


def menu_hub(request):
    return render(request, 'menu/menu.html', {'lunchs'  : Lunch.objects.all(), 
                                              'menus'   : Menu.objects.all(),
                                              'meals'   : Meal.objects.all(),
                                              'salads'  : Salad.objects.all(),
                                              'desserts': Dessert.objects.all()})

def menus_day(request, menu_uuid):
    try:
        check_time = datetime.datetime.now()
        if check_time.hour < 11:
            if request.method == 'POST':

                new_order = Order(day=check_time, 
                                lunch=Lunch.objects.get(id=request.POST.dict()['lunchs']),
                                comment=request.POST.dict()['comment'],
                                employee=Employee.objects.get(uuid=menu_uuid))
                new_order.save()
                return HttpResponse("Thanks For Order with Nora's Lunch")

            select_menu = {'menusday': SelectMenuForm()}
            return render(request, 'menu/select_menu.html', select_menu)
        else:
            return HttpResponse("too late")
    except Exception as error:
        return HttpResponse(error)

def send_message(request, menu_id):

    for employee in Employee.objects.all():
        try:
            response = client.chat_postMessage(channel=employee.slack_id , text=Menu.objects.get(id=menu_id).generate_slack_message(employee.uuid))
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")

    return redirect(menu_hub)

# CREATE VIEWS
def create_menu(request):
    # TODO send a popup message if fail or success
    # TODO block two menus for the same day
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
    menu_form = {'menuform': MenuForm()}
    return render(request, 'menu/create_menu.html', menu_form) 

def create_lunch(request):

    # TODO send a popup message if fail or success
    if request.method == 'POST':
        form = LunchForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'menu/create_lunch.html', {'lunchform'  : LunchForm() })

def create_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'menu/create_meal.html', {'mealform'  : MealForm() })

def create_salad(request):
    if request.method == 'POST':
        form = SaladForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'menu/create_salad.html', {'saladform'  : SaladForm() })

def create_dessert(request):
    if request.method == 'POST':
        form = DessertForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'menu/create_dessert.html', {'dessertform'  : DessertForm() })


# UPDATE VIEWS
def update_menu(request, pk):
    menu = Menu.objects.get(id=pk)
    form = MenuForm(instance=menu)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect(menu_hub)

    menu_form = {'menuform': form}
    return render(request, 'menu/create_menu.html', menu_form) 

def update_lunch(request, pk):
    lunch = Lunch.objects.get(id=pk)
    form = LunchForm(instance=lunch)
    if request.method == 'POST':
        form = LunchForm(request.POST, instance=lunch)
        if form.is_valid():
            form.save()
            return redirect(menu_hub)

    lunchform = {'lunchform': form}
    return render(request, 'menu/create_lunch.html', lunchform) 

def update_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    form = MealForm(instance=meal)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect(menu_hub)

    mealform = {'mealform': form}
    return render(request, 'menu/create_meal.html', mealform) 

def update_salad(request, pk):
    salad = Salad.objects.get(id=pk)
    form = SaladForm(instance=salad)
    if request.method == 'POST':
        form = SaladForm(request.POST, instance=salad)
        if form.is_valid():
            form.save()
            return redirect(menu_hub)

    saladform = {'saladform': form }
    return render(request, 'menu/create_salad.html', saladform) 

def update_dessert(request, pk):
    dessert = Dessert.objects.get(id=pk)
    form = DessertForm(instance=dessert)
    if request.method == 'POST':
        form = DessertForm(request.POST, instance=dessert)
        if form.is_valid():
            form.save()
            return redirect(menu_hub)

    dessertform = {'dessertform': form}
    return render(request, 'menu/create_dessert.html', dessertform) 


# DELETE VIEWS
def delete_menu(request, pk):
    menu = Menu.objects.get(id=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect(menu_hub)

    form = {'item': menu}
    return render(request, "menu/delete_menu.html", form)

def delete_lunch(request, pk):
    lunch = Lunch.objects.get(id=pk)
    if request.method == 'POST':
        lunch.delete()
        return redirect(menu_hub)
        
    form = {'item': lunch}
    return render(request, "menu/delete_lunch.html", form)

def delete_meal(request, pk):
    meal = Meal.objects.get(id=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect(menu_hub)
        
    form = {'item': meal}
    return render(request, "menu/delete_meal.html", form)

def delete_salad(request, pk):
    salad = Salad.objects.get(id=pk)
    if request.method == 'POST':
        salad.delete()
        return redirect(menu_hub)
        
    form = {'item': salad}
    return render(request, "menu/delete_salad.html", form)

def delete_dessert(request, pk):
    dessert = Dessert.objects.get(id=pk)
    if request.method == 'POST':
        dessert.delete()
        return redirect(menu_hub)
        
    form = {'item': dessert}
    return render(request, "menu/delete_lunch.html", form)

