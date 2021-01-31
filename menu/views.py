from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse("This is the menu page")

def create(request):
    return HttpResponse("This is were the menus/meals/salad/dessert will be created")
