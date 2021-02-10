from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from employees.models import Employee
from hamcrest import *

class TestsEmployeesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')

        self.employee_hub    = reverse('employee_hub')
        self.create_employee = reverse('create_employee')

    
    def tearDown(self):
        self.user.delete()

    def tests_employee_hub_GET(self):
        response = self.client.get(self.employee_hub)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'employees/menu.html')


    def tests_create_employee_GET(self):
        response = self.client.get(self.create_employee)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'employees/create_employee.html')

    def tests_create_employee_POST(self):
        name     = "testingName"
        slack_id = "GDFMK74IH"
        response = self.client.post(self.create_employee, {'name'     : name,
                                                           'slack_id' : slack_id})
        assert_that(response.status_code, equal_to(200))
        assert_that(Employee.objects.first().name, equal_to(name))
        assert_that(Employee.objects.first().slack_id, equal_to(slack_id))
        self.assertTemplateUsed(response, 'employees/create_employee.html')


    def tests_update_employee_GET(self):
        Employee.objects.create(name= "Testing",
                                slack_id="JNDFK8745")
        update_employee = reverse('update_employee', args=[Employee.objects.first().uuid])
        
        response = self.client.get(update_employee)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'employees/create_employee.html')

    def tests_update_employee_POST(self):
        
        Employee.objects.create(name= "Testing",
                                slack_id="JNDFK8745")
        update_employee = reverse('update_employee', args=[Employee.objects.first().uuid])
        
        change_name = "Changing"
        response = self.client.post(update_employee, data={'name': change_name, 
                                                           'slack_id' : Employee.objects.first().slack_id})
        
        assert_that(response.status_code, equal_to(302))
        assert_that(Employee.objects.first().name, equal_to(change_name))

    def tests_delete_employee_get(self):
        
        Employee.objects.create(name= "Testing",
                                slack_id="JNDFK8745")
        delete_employee = reverse('delete_employee', args=[Employee.objects.first().uuid])

        response = self.client.get(delete_employee)
        
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'employees/delete_employee.html')


    def tests_delete_employee_POST(self):
        
        Employee.objects.create(name= "Testing",
                                slack_id="JNDFK8745")
        delete_employee = reverse('delete_employee', args=[Employee.objects.first().uuid])
        
        change_name = "Changing"
        response = self.client.post(delete_employee, data={'name': Employee.objects.first().name, 
                                                           'slack_id' : Employee.objects.first().slack_id})
        
        assert_that(response.status_code, equal_to(302))
        assert_that(Employee.objects.count(), equal_to(0))