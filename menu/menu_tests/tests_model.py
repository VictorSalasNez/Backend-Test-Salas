from menu.models import Meal, Salad, Dessert, Lunch, Menu, Order, MENU_TYPE
from django.test import TestCase
from hamcrest import *
import uuid
# Create your tests here.

class TestEmployee(TestCase):
    def setUp(self):
        self.meal_name = "Porotos"
        self.salad_name = "Tomates"
        self.dessert_name = "Helado"
        self.salad_name = "Tomates"
        self.comment_menu = "Some Comment"
        self.empty = ""

    def test_meal_str(self):
        meal = Meal(meal_name=self.meal_name, category=MENU_TYPE[1][1])
        assert_that(str(meal), equal_to(self.meal_name))
    
    def test_salad_str(self):
        salad = Salad(salad_name=self.salad_name)
        assert_that(str(salad), equal_to(self.salad_name))

    def test_dessert_str(self):
        dessert = Dessert(dessert_name=self.dessert_name, category=MENU_TYPE[1][1])
        assert_that(str(dessert), equal_to(self.dessert_name))

    def test_lunch_str_category(self):
        meal = Meal(meal_name=self.meal_name, category=MENU_TYPE[1][1])
        salad = Salad(salad_name=self.salad_name)
        dessert = Dessert(dessert_name=self.dessert_name, category=MENU_TYPE[1][1])
        category = MENU_TYPE[1][1]
        lunch = Lunch(meal=meal, salad=salad, dessert=dessert, category=category)

        assert_that(str(lunch), equal_to(f"({category}) -> {meal}, {salad}, {dessert}"))

    def test_lunch_str_no_category(self):
        meal = Meal(meal_name=self.meal_name, category=MENU_TYPE[1][1])
        salad = Salad(salad_name=self.salad_name)
        dessert = Dessert(dessert_name=self.dessert_name, category=MENU_TYPE[1][1])
        lunch = Lunch(meal=meal, salad=salad, dessert=dessert)

        assert_that(str(lunch), equal_to(f"{meal}, {salad}, {dessert}"))
