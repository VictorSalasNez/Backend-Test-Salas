from menu.models import Meal, Salad, Dessert, Lunch, Menu, Order, MENU_TYPE
from django.test import TestCase
from hamcrest import *
from datetime import datetime
import uuid
# Create your tests here.

class TestMenuModels(TestCase):
    
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
        self.model_menu         = Menu.objects.create(day=datetime(2021,11,11).strftime("%Y-%m-%d"))
        self.model_menu_w_menu  = Menu.objects.create(day=datetime(2021,11,11).strftime("%Y-%m-%d"))
        self.model_menu_w_menu.lunchs.add(self.model_lunch_cat)
        self.model_menu_w_menu.lunchs.add(self.model_lunch_no_cat)




    def test_meal_str(self):
        assert_that(str(self.model_meal), equal_to(self.meal_name))
    
    def test_salad_str(self):
        assert_that(str(self.model_salad), equal_to(self.salad_name))

    def test_dessert_str(self):
        assert_that(str(self.model_dessert), equal_to(self.dessert_name))

    def test_lunch_str_category(self):
        assert_that(str(self.model_lunch_cat), equal_to(f"({self.category}) -> {self.model_meal}, {self.model_salad}, {self.model_dessert}"))

    def test_lunch_str_no_category(self):
        assert_that(str(self.model_lunch_no_cat), equal_to(f"{self.model_meal}, {self.model_salad}, {self.model_dessert}"))

    def test_menu_generate_str_options_no_lunchs(self):
        assert_that(self.model_menu.generate_str_options(),equal_to(self.empty) )

    def test_menu_generate_str_options(self):
        assert_that(self.model_menu_w_menu.generate_str_options(),
                    equal_to(f"Option 1: {self.model_lunch_cat}\nOption 2: {self.model_lunch_no_cat}\n") )

    def test_generate_url_menu(self):
        assert_that(self.model_menu.generate_url_menu(self.uuid), contains_string(f"menu/{self.uuid}"))
    
    def test_generate_slack_message(self):
        assert_that(self.model_menu_w_menu.generate_slack_message(self.uuid),
                    contains_string("Hello!\nI share with you today's menu :)\n\n"),
                    contains_string("\nChoose your menu here: "))

    def test_diplay_lunches(self):
        assert_that(self.model_menu_w_menu.diplay_lunches, instance_of(list))
        assert_that(self.model_menu_w_menu.diplay_lunches, has_length(2))
        assert_that(self.model_menu_w_menu.diplay_lunches,
                    contains_inanyorder(str(self.model_lunch_cat), 
                                        str(self.model_lunch_no_cat)) )


    
