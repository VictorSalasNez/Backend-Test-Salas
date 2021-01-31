from django.db import models

# Create your models here.

class Meal(models.Model):
    """
    Class that represent a Meal

    Attributes:
        meal_name (string): name of the meal (max 80)
    """
    meal_name = models.CharField(max_length=80, null=True)

    def __str__(self):
        return self.meal_name

class Salad(models.Model):
    """
    Class that represent a Salad

    Attributes:
        salad_name (string): name of the salad (max 80)
    """
    salad_name = models.CharField(max_length=80, null=True) 

    def __str__(self):
        return self.salad_name

class Dessert(models.Model):
    """
    Class that represent a Dessert

    Attributes:
        dessert_name (string): name of the dessert (max 80)
    """
    dessert_name = models.CharField(max_length=80, null=True) 
    
    def __str__(self):
        return self.dessert_name

class Menu(models.Model):
    """
    Class that represent a Menu

    Attributes:
        meal    (int): foreing key of the id meal
        salad   (int): foreing key of the id salad
        dessert (int): foreing key of the id dessert
    """
    meal    = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    salad   = models.ForeignKey(Salad, on_delete=models.CASCADE, null=True)
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f"{self.meal}, {self.salad}, {self.dessert}"