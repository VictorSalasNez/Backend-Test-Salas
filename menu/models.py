from django.db import models

# Create your models here.

MENU_TYPE = (
                ('Carnivoro', 'Carnivoro'),
                ('Vegetariano', 'Vegetariano'),
                ('Vegano', 'Vegano')
            )

class Meal(models.Model):
    """
    Class that represent a Meal

    Attributes:
        meal_name (string): name of the meal (max 80)
    """
    
    meal_name = models.CharField(max_length=80, null=True)
    category  = models.CharField(max_length=80, null=True, choices=MENU_TYPE)

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
    category     = models.CharField(max_length=80, null=True, choices=MENU_TYPE)
    
    def __str__(self):
        return self.dessert_name

class Lunch(models.Model):
    """
    Class that represent a Lunch with is meal, salad and dessert

    Attributes:
        meal    (int): foreing key of the id meal
        salad   (int): foreing key of the id salad
        dessert (int): foreing key of the id dessert
    """

    meal      = models.ForeignKey(Meal, on_delete=models.CASCADE, null=True)
    salad     = models.ForeignKey(Salad, on_delete=models.CASCADE, null=True)
    dessert   = models.ForeignKey(Dessert, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=200, null=True, choices=MENU_TYPE)


    def __str__(self):
        lunch_type = "" if self.category is None else f"({self.category}) -> "
        return f"{lunch_type}{self.meal}, {self.salad}, {self.dessert}"


class Menu(models.Model):
    """
    Class that represent a menu of a day

    Attributes:
        day     (date) : day of this menu
        lunch   (int)  : multiple lunch assosiated with this menu
    """

    day    = models.DateField()
    lunchs = models.ManyToManyField(Lunch)

    def generate_slack_message(self):
        options = ''
        for num, lunch in zip( range(self.lunchs), self.lunchs):
            options += f"Option {num+1}: {lunch}\n"

        return f"Hello!\nI share with you today's menu :)\n\n{options}\nHave a nice day!"""

    @property
    def diplay_lunches(self):
        lunches_str = []
        for lunch in self.lunchs.values():
            lunch_id = lunch["id"]
            lunches_str.append(f"{Lunch.objects.get(id=lunch_id)}")

        return lunches_str