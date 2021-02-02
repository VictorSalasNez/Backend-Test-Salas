from django.forms import ModelForm
from .models import Meal, Salad, Dessert, Lunch, Menu

class MealForm(ModelForm):
    class Meta:
        model  = Meal
        fields = '__all__'

class SaladForm(ModelForm):
    class Meta:
        model  = Salad
        fields = '__all__'

class DessertForm(ModelForm):
    class Meta:
        model  = Dessert
        fields = '__all__'

class LunchForm(ModelForm):
    class Meta:
        model  = Lunch
        fields = '__all__'


class MenuForm(ModelForm):
    class Meta:
        model  = Menu
        fields = '__all__'