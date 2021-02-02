from django.forms import ModelForm
from .models import Meal, Salad, Dessert, Lunch

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