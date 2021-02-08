from django.test import TestCase
from employees.models import Employee
import uuid
# Create your tests here.

class TestEmployee(TestCase):
    def setUp(self):
        self.name = "Victor"
        self.slack_id = "LISDILJG"
        self.empty = ""
        self.model_basic = Employee(name=self.name, slack_id=self.slack_id)

    def tests_employee_model_str(self):
        self.assertEqual(str(self.model_basic),self.name)