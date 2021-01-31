from django.db import models

# Create your models here.

class Employee(models.Model):
    """
    Class that represent a Meal

    Attributes:
        id_employee (int): idenfitier of the employee
        name        (str): 
        slack_id    (str):
    """
    name        = models.CharField(max_length=80)
    slack_id    = models.CharField(max_length=80)