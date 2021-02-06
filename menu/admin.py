from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Meal)
admin.site.register(Salad)
admin.site.register(Dessert)
admin.site.register(Lunch)
admin.site.register(Menu)
admin.site.register(Order)