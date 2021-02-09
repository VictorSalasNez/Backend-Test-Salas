from django.test import TestCase
from main.forms import CreateUser
from hamcrest import *
from django.contrib.auth.models import User
# Create your tests here.

class TestCreateUser(TestCase):
    
    def setUp(self):
        self.name = "Victor"
        self.email_good = "some_email@gmail.com"
        self.email_bad = "some_emailgmail.com"
        self.passwords_strong = "SomeAwesome.Password"
        self.passwords_week = "1234"
        self.empty_name = ""
        self.form_basic = CreateUser()

    def tests_createuser_fields(self):
        assert_that(self.form_basic.fields, has_key("username"))
        assert_that(self.form_basic.fields, has_key("email"))
        assert_that(self.form_basic.fields, has_key("password1"))
        assert_that(self.form_basic.fields, has_key("password2"))

    def tests_createuser_no_fields(self):
        assert_that(self.form_basic.fields.get("uuid"), equal_to(None))

    def tests_createuser_model_instance(self):
        assert_that(self.form_basic.Meta.model, equal_to(User))

    def tests_createuser_form_good(self):
        form = CreateUser(data= {"username": self.name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_strong,
                                 "password2": self.passwords_strong })

        assert_that(form.is_valid(), equal_to(True))
        assert_that(form.data["username"], equal_to(self.name))
        assert_that(form.data["email"], equal_to(self.email_good))
        assert_that(form.data["password1"], equal_to(self.passwords_strong))
        assert_that(form.data["password2"], equal_to(self.passwords_strong))

    def tests_createuser_form_no_name(self):
        form = CreateUser(data= {"username": self.empty_name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_strong,
                                 "password2": self.passwords_strong })

        assert_that(form.is_valid(), equal_to(False))
    
    def tests_createuser_form_week_pass(self):
        form = CreateUser(data= {"username": self.name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_week,
                                 "password2": self.passwords_strong })
        assert_that(form.is_valid(), equal_to(False))

    def tests_createuser_form_nothing(self):
        form = CreateUser(data= {})
        assert_that(form.is_valid(), equal_to(False))
    