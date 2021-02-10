from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib import messages
from django.urls import reverse
from hamcrest import *

class TestsEmployeesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.main     = reverse('Noras Dasboard')
        self.register = reverse('Register_page')
        self.login    = reverse('Login_page')
        self.logout   = reverse('Logout_page')

        self.name = "vxs251"
        self.email = "asdgg@gmail.com"
        self.pass1 = "hola.que.tal"
        self.pass2 = "hola.que.tal"

    def test_dashboard_get(self):
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')
        response = self.client.get(self.main)        
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'main/main.html')


    def test_dashboard_get_no_auth(self):
        response = self.client.get(self.main)        
        assert_that(response.status_code, equal_to(302))


    def test_register_already_is_authenticated(self):
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')
        response = self.client.get(self.register)
        assert_that(response.status_code, equal_to(302))
        self.user.delete()
        self.client.logout()
    
    def tests_register_get(self):
        response = self.client.get(self.register)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'main/register.html')


    def tests_register_post(self):
        assert_that(User.objects.count(), equal_to(0))
        response = self.client.post(self.register, data={'username':self.name,
                                                         'email':self.email,
                                                         'password1':self.pass1,
                                                         'password2':self.pass2})
                                            
        assert_that(response.status_code, equal_to(302))
        assert_that(User.objects.count(), equal_to(1))
    
    def test_login_page_already_is_authenticated(self):
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')
        response = self.client.get(self.login)
        assert_that(response.status_code, equal_to(302))
        self.user.delete()
        self.client.logout()       

    def test_login_get(self):
        response = self.client.get(self.login)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'main/login.html')
    

    def test_login_correct_post(self):
        name = "tests"
        passw = "12test12"
        self.user = User.objects.create_user(username = name,
                                             password = passw,
                                             email='test@example.com')

        response = self.client.post(self.login, data={'username': name , 
                                                      'password': passw})
        assert_that(response.status_code, equal_to(302))


    def test_login_bad_post(self):
        name = "tests"
        passw = "badpass"
        response = self.client.post(self.login, data={'username': name , 
                                                      'password': passw})
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'main/login.html')

    def test_logout_get(self):
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')
        response = self.client.get(self.logout)
        assert_that(response.status_code, equal_to(302))
    
    def test_logout_get_no_login(self):
        
        response = self.client.get(self.logout)
        assert_that(response.status_code, equal_to(302))
    
    