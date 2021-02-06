from django.shortcuts import render
from menu.models import Order, Menu
from datetime import date
# Create your views here.


def dashboard(request):
    return render(request, 'main/main.html', {'orders': Order.objects.all(), 
                                              'today_day': date.today().day,
                                              'menus': Menu.objects.all().order_by('day')})