from menu.models import Meal, Salad, Dessert, Lunch, Menu, Order, MENU_TYPE
from menu.forms import SelectMenuForm
from datetime import datetime
from django.test import TestCase
from hamcrest import *
import uuid
# Create your tests here.

class TestMenuForms(TestCase):

    def setUp(self):
        # Basic Names
        self.meal_name    = "Porotos"
        self.salad_name   = "Tomates"
        self.dessert_name = "Helado"
        self.salad_name   = "Tomates"
        self.comment_menu = "Some Comment"
        self.empty        = ""
        self.uuid         = "112233"

        # Basic Models
        self.category           = category = MENU_TYPE[1][1]
        self.model_meal         = Meal.objects.create(meal_name=self.meal_name, category=self.category )
        self.model_salad        = Salad.objects.create(salad_name=self.salad_name)
        self.model_dessert      = Dessert.objects.create(dessert_name=self.dessert_name, category=self.category )
        self.model_lunch_cat    = Lunch.objects.create(meal=self.model_meal, salad=self.model_salad, dessert=self.model_dessert, category=self.category )
        self.model_lunch_no_cat = Lunch.objects.create(meal=self.model_meal, salad=self.model_salad, dessert=self.model_dessert)
        self.model_menu_w_menu  = Menu.objects.create(day=datetime.now().strftime("%Y-%m-%d"))
        self.model_menu_w_menu.lunchs.add(self.model_lunch_cat)
        self.model_menu_w_menu.lunchs.add(self.model_lunch_no_cat)

    def test_SelectMenuForm_fields(self):
        form = SelectMenuForm()
        assert_that(form.fields, has_key("comment"))
        