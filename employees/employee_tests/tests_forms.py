from django.test import TestCase
from employees.forms import EmployeeForm
from employees.models import Employee
from hamcrest import *
# Create your tests here.

class TestEmployeeForms(TestCase):
    
    def setUp(self):
        self.name = "Victor"
        self.slack_id = "LISDILJG"
        self.empty = ""
        self.form_basic = EmployeeForm()

    def tests_employee_fields(self):
        assert_that(self.form_basic.fields, has_key("name"))
        assert_that(self.form_basic.fields, has_key("slack_id"))

    def tests_employee_no_fields(self):
        assert_that(self.form_basic.fields.get("uuid"), equal_to(None))

    def tests_employee_model_instance(self):
        assert_that(self.form_basic.Meta.model, equal_to(Employee))

    def tests_employe_form_good(self):
        form = EmployeeForm(data= {"name": self.name , "slack_id": self.slack_id})
        assert_that(form.is_valid(), equal_to(True))
        assert_that(form.data["name"], self.name)
        assert_that(form.data["slack_id"], self.slack_id)

    def tests_employe_form_no_name(self):
        form = EmployeeForm(data= {"name": self.empty , "slack_id": self.slack_id})
        assert_that(form.is_valid(), equal_to(False))
    
    def tests_employe_form_no_slack_id(self):
        form = EmployeeForm(data= {"name": self.name , "slack_id": self.empty})
        assert_that(form.is_valid(), equal_to(False))

    def tests_employe_form_nothing(self):
        form = EmployeeForm(data= {"name": self.empty , "slack_id": self.empty})
        assert_that(form.is_valid(), equal_to(False))
    