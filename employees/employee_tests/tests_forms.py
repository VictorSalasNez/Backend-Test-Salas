from django.test import TestCase
from employees.forms import EmployeeForm
from employees.models import Employee
# Create your tests here.

class TestEmployeeForms(TestCase):
    
    def setUp(self):
        self.name = "Victor"
        self.slack_id = "LISDILJG"
        self.empty = ""
        self.form_basic = EmployeeForm()

    def tests_employee_fields(self):
        self.assertTrue(self.form_basic.fields.get("name"))
        self.assertTrue(self.form_basic.fields.get("slack_id"))

    def tests_employee_no_fields(self):
        self.assertIsNone(self.form_basic.fields.get("uuid"))

    def tests_employee_model_instance(self):
        self.assertEqual(self.form_basic.Meta.model, Employee)

    def tests_employe_form_good(self):
        form = EmployeeForm(data= {"name": self.name , "slack_id": self.slack_id})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.data["name"], self.name)
        self.assertEqual(form.data["slack_id"], self.slack_id)

    def tests_employe_form_no_name(self):
        form = EmployeeForm(data= {"name": self.empty , "slack_id": self.slack_id})
        self.assertFalse(form.is_valid())
    
    def tests_employe_form_no_slack_id(self):
        form = EmployeeForm(data= {"name": self.name , "slack_id": self.empty})
        self.assertFalse(form.is_valid())

    def tests_employe_form_nothing(self):
        form = EmployeeForm(data= {"name": self.empty , "slack_id": self.empty})
        self.assertFalse(form.is_valid())
    