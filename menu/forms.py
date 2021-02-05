from django.forms import ModelForm, ChoiceField
from datetime import date
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
    #TODO find a way to display a datepicker
    class Meta:
        model  = Menu
        fields = '__all__'


class SelectMenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ['lunchs']

    def __init__(self):
        super(SelectMenuForm, self).__init__()
        menu_list = Menu.objects.get(day=date.today()).generate_str_options().split("\n")[:-1]
        OPTIONS = tuple([(lunch, lunch) for lunch in menu_list])
        self.fields['lunchs'] = ChoiceField(required=True, choices=OPTIONS)

