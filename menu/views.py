from django.shortcuts import render, redirect
from django.http import HttpResponse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
# Create your views here.
from .models import Lunch, Menu
from .forms import MealForm, SaladForm, DessertForm, LunchForm, MenuForm
from employees.models import Employee

os.environ['SLACK_BOT_TOKEN'] = "xoxb-1691797685303-1708676997845-jtGFddMOhEDsscCcjMqRUfw9"
client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

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