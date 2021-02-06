from django.db import models
import uuid
# Create your models here.

class Employee(models.Model):
    """
    Class that represent a Meal

    Attributes:
        name        (str):
        slack_id    (str):
    """
    uuid     = models.UUIDField(primary_key = True, 
                                default = uuid.uuid4, 
                                editable = False)
    name     = models.CharField(max_length=80, null=True)
    slack_id = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.name