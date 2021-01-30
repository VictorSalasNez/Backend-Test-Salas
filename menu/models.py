from django.db import models

# Create your models here.

class Meal(models.Model):
    """
    Class that represent a Meal

    Attributes:
        id_meal   (int)   : idenfitier of the meal
        meal_name (string): name of the meal (max 80)
    """
    id_meal   = models.AutoField(primary_key=True)
    meal_name = models.CharField(max_length=80) 

class Salad(models.Model):
    """
    Class that represent a Salad

    Attributes:
        id_salad   (int)   : idenfitier of the salad
        salad_name (string): name of the salad (max 80)
    """
    id_salad   = models.AutoField(primary_key=True)
    salad_name = models.CharField(max_length=80) 

class Dessert(models.Model):
    """
    Class that represent a Dessert

    Attributes:
        id_dessert   (int)   : idenfitier of the dessert
        dessert_name (string): name of the dessert (max 80)
    """
    id_dessert   = models.AutoField(primary_key=True)
    dessert_name = models.CharField(max_length=80) 

class Menu(models.Model):
    """
    Class that represent a Menu

    Attributes:
        id_menu (int): idenfitier of the menu
        meal    (int): foreing key of the id meal
        salad   (int): foreing key of the id salad
        dessert (int): foreing key of the id dessert
    """
    id_menu = models.AutoField(primary_key=True)
    meal    = models.ForeignKey(Meal, on_delete=models.CASCADE)
    salad   = models.ForeignKey(Salad, on_delete=models.CASCADE)
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE)