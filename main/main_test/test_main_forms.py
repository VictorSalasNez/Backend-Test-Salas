from django.test import TestCase
from main.forms import CreateUser
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
        self.assertTrue(self.form_basic.fields.get("username"))
        self.assertTrue(self.form_basic.fields.get("email"))
        self.assertTrue(self.form_basic.fields.get("password1"))
        self.assertTrue(self.form_basic.fields.get("password2"))

    def tests_createuser_no_fields(self):
        self.assertIsNone(self.form_basic.fields.get("uuid"))

    def tests_createuser_model_instance(self):
        self.assertEqual(self.form_basic.Meta.model, User)

    def tests_createuser_form_good(self):
        form = CreateUser(data= {"username": self.name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_strong,
                                 "password2": self.passwords_strong })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data["username"], self.name)
        self.assertEqual(form.data["email"], self.email_good)
        self.assertEqual(form.data["password1"], self.passwords_strong)
        self.assertEqual(form.data["password2"], self.passwords_strong)

    def tests_createuser_form_no_name(self):
        form = CreateUser(data= {"username": self.empty_name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_strong,
                                 "password2": self.passwords_strong })

        self.assertFalse(form.is_valid())
    
    def tests_createuser_form_week_pass(self):
        form = CreateUser(data= {"username": self.name , 
                                 "email": self.email_good,
                                 "password1": self.passwords_week,
                                 "password2": self.passwords_strong })
        self.assertFalse(form.is_valid())

    def tests_createuser_form_nothing(self):
        form = CreateUser(data= {})
        self.assertFalse(form.is_valid())
    