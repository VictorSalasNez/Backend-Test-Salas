from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from menu.models import *
from hamcrest import *

class TestsEmployeesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test',
                                             password='12test12',
                                             email='test@example.com')
        self.user.save()
        self.client.login(username='test', password='12test12')
        
        self.menu_hub    = reverse('menu_hub')

        #self.menus_day   = reverse('Nora_Menu')

        self.create_menu    = reverse('Create_Menu_Page')
        self.create_lunch   = reverse('Create_Lunch_Page')
        self.create_meal    = reverse('Create_Meal_Page')
        self.create_salad   = reverse('Create_Salad_Page')
        self.create_dessert = reverse('Create_Dessert_Page')

        #self.update_lunch   = reverse('Update_Lunch_Page')
        #self.update_menu    = reverse('Update_Menu_Page')


        #self.delete_lunch   = reverse('Delete_lunch')
        #self.delete_menu    = reverse('Delete_menu')
        #self.delete_meal    = reverse('Delete_meal')
        #self.delete_salad   = reverse('Delete_salad')
        #self.delete_dessert = reverse('Delete_dessert')

        #self.send_message   = reverse('Send_Message')

    def test_menu_hub(self):
        response = self.client.get(self.menu_hub)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/menu.html')

    #CREATE VIEWS

    def test_create_menu_get(self):
        response = self.client.get(self.create_menu)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_menu.html')
    
    def test_create_menu_post_no_valid(self):
        assert_that(Menu.objects.count(), equal_to(0))
        response = self.client.post(self.create_menu, {'day': datetime.now().strftime("%Y-%m-%d"),
                                                       'lunchs': ""})
        assert_that(Menu.objects.count(), equal_to(0))
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_menu.html')

    def test_create_menu_post_valid(self):

        dessert_name= "name dessert"
        meal_name = "meal name"
        salad_name = "name salad"
        dessert_name_2= "name dessert 2"
        meal_name_2 = "meal name 2"
        salad_name_2 = "name salad 2"

        Meal.objects.get_or_create(meal_name=meal_name,
                            category = MENU_TYPE[1][1])
        Salad.objects.get_or_create(salad_name=salad_name)
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])

        Meal.objects.get_or_create(meal_name=meal_name_2,
                            category = MENU_TYPE[1][1])
        Salad.objects.get_or_create(salad_name=salad_name_2)
        Dessert.objects.get_or_create(dessert_name=dessert_name_2,
                                      category=MENU_TYPE[1][1])

        Lunch.objects.get_or_create(meal=Meal.objects.get(id=1),
                                    salad=Salad.objects.get(id=1),
                                    dessert=Dessert.objects.get(id=1),
                                    category=MENU_TYPE[1][1])
        
        Lunch.objects.get_or_create(meal=Meal.objects.get(id=2),
                                    salad=Salad.objects.get(id=2),
                                    dessert=Dessert.objects.get(id=2),
                                    category=MENU_TYPE[1][1])

        assert_that(Menu.objects.count(), equal_to(0))
        response = self.client.post(self.create_menu, data={'day': datetime.now().strftime("%Y-%m-%d"),
                                                            'lunchs': [Lunch.objects.get(id=1).id, Lunch.objects.get(id=2).id]})
        assert_that(Menu.objects.count(), equal_to(1))
        assert_that(len(Menu.objects.first().lunchs.all()), equal_to(2) )

        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_menu.html')

    def test_create_lunch_get(self):
        response = self.client.get(self.create_lunch)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_lunch.html')

    def test_create_lunch_post_no_valid(self):
        dessert_name= "name dessert"
        meal_name = "meal name"
        salad_name = "name salad"
        Salad.objects.get_or_create(salad_name=salad_name)
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])

        assert_that(Lunch.objects.count(), equal_to(0))   
        response = self.client.post(self.create_lunch, {'meal': "",
                                                        'salad': Salad.objects.first().id,
                                                        'dessert': Dessert.objects.first().id,
                                                        'category': MENU_TYPE[1][1]})
        assert_that(Lunch.objects.count(), equal_to(0)) 
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_lunch.html')

    def test_create_lunch_post_valid(self):
        dessert_name= "name dessert"
        meal_name = "meal name"
        salad_name = "name salad"
        Meal.objects.get_or_create(meal_name=meal_name,
                            category = MENU_TYPE[1][1])
        Salad.objects.get_or_create(salad_name=salad_name)
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])

        assert_that(Lunch.objects.count(), equal_to(0))   
        response = self.client.post(self.create_lunch, {'meal': Meal.objects.first().id,
                                                        'salad': Salad.objects.first().id,
                                                        'dessert': Dessert.objects.first().id,
                                                        'category': MENU_TYPE[1][1]})
        assert_that(Lunch.objects.count(), equal_to(1)) 
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_lunch.html')

    def test_create_meal_get(self):
        response = self.client.get(self.create_meal)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_meal.html')
    
    def test_create_meal_post(self):
        meal = 'some meal'
        response = self.client.post(self.create_meal, {'meal_name': meal,
                                                       'category': MENU_TYPE[1][1]})
        assert_that(response.status_code, equal_to(200))
        assert_that(Meal.objects.count(), equal_to(1))
        assert_that(Meal.objects.first().meal_name, equal_to(meal))
        assert_that(Meal.objects.first().category, equal_to(MENU_TYPE[1][1]))
        self.assertTemplateUsed(response, 'menu/create_meal.html')

    def test_create_salad_get(self):
        response = self.client.get(self.create_salad)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_salad.html')
    
    def test_create_salad_post(self):
        salad = "salad_name"
        response = self.client.post(self.create_salad, {'salad_name':salad})
        assert_that(response.status_code, equal_to(200))
        assert_that(Salad.objects.count(), equal_to(1))
        assert_that(Salad.objects.first().salad_name, equal_to(salad))
        self.assertTemplateUsed(response, 'menu/create_salad.html')

    def test_create_dessert_get(self):
        response = self.client.get(self.create_dessert)
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_dessert.html')
    
    def test_create_dessert_post(self):
        dessert = "dessert"
        response = self.client.post(self.create_dessert, {'dessert_name':dessert,
                                                          'category': MENU_TYPE[1][1]})
        assert_that(Dessert.objects.count(), equal_to(1))
        assert_that(Dessert.objects.first().dessert_name, equal_to(dessert))
        assert_that(Dessert.objects.first().category, equal_to(MENU_TYPE[1][1]))
        assert_that(response.status_code, equal_to(200))
        self.assertTemplateUsed(response, 'menu/create_dessert.html')

    #UPDATE VIEWS

    def test_update_menu_get(self):
        pass

    def test_update_menu_post(self):
        pass

    def test_update_lunch_get(self):
        dessert_name= "name dessert"
        meal_name = "meal name"
        salad_name = "name salad"
        Meal.objects.get_or_create(meal_name=meal_name,
                            category = MENU_TYPE[1][1])
        Salad.objects.get_or_create(salad_name=salad_name)
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])

        Lunch.objects.get_or_create(meal=Meal.objects.get(id=1),
                                    salad=Salad.objects.get(id=1),
                                    dessert=Dessert.objects.get(id=1),
                                    category=MENU_TYPE[1][1])

        update_lunch = reverse('Update_Lunch_Page', args=[Lunch.objects.first().id])


    def test_update_lunch_post(self):
        dessert_name = "name dessert"
        meal_name = "meal name"
        salad_name = "name salad"
        dessert_name_2 = "updated_name"
        Meal.objects.get_or_create(meal_name=meal_name,
                            category = MENU_TYPE[1][1])
        Salad.objects.get_or_create(salad_name=salad_name)
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])

        Dessert.objects.get_or_create(dessert_name=dessert_name_2,
                                      category=MENU_TYPE[1][1])

        Lunch.objects.get_or_create(meal=Meal.objects.get(id=1),
                                    salad=Salad.objects.get(id=1),
                                    dessert=Dessert.objects.get(id=1),
                                    category=MENU_TYPE[1][1])



        update_lunch = reverse('Update_Lunch_Page', args=[Lunch.objects.first().id])

        response = self.client.post(update_lunch, {'meal': Meal.objects.get(id=1),
                                                   'salad': Salad.objects.get(id=1),
                                                   'dessert': Dessert.objects.get(id=2),
                                                   'category' : MENU_TYPE[1][1]})

        assert_that(response.status_code, equal_to(302))

        assert_that(Lunch.objects.first().dessert.dessert_name, equal_to(dessert_name_2))








    def test_update_meal_get(self):
        meal_name= "name meal"
        Meal.objects.get_or_create(meal_name=meal_name,
                                   category = MENU_TYPE[1][1])
        
        update_meal = reverse('Update_Meal_Page', args=[Meal.objects.first().id])

        response = self.client.get(update_meal)
        assert_that(response.status_code, equal_to(200))

        assert_that(Meal.objects.first().meal_name, equal_to(meal_name))
        assert_that(Meal.objects.first().category, equal_to(MENU_TYPE[1][1]))

        self.assertTemplateUsed(response, 'menu/create_meal.html')


    def test_update_meal_post(self):
        meal_name= "name meal"
        Meal.objects.get_or_create(meal_name=meal_name,
                                   category = MENU_TYPE[1][1])

        assert_that(Meal.objects.count(), equal_to(1))
        assert_that(Meal.objects.first().meal_name, equal_to(meal_name))
        assert_that(Meal.objects.first().category, equal_to(MENU_TYPE[1][1]))

        update_meal = reverse('Update_Meal_Page', args=[Meal.objects.first().id])

        update_name = "updated_meal"
        update_category = MENU_TYPE[0][0]
        response = self.client.post(update_meal, {'meal_name': update_name,
                                                  'category' : update_category})

        assert_that(response.status_code, equal_to(302))
        assert_that(Meal.objects.count(), equal_to(1))
        assert_that(Meal.objects.first().meal_name, equal_to(update_name))
        assert_that(Meal.objects.first().category, equal_to(update_category))

    def test_update_salad_get(self):
        salad_name= "name salad"
        Salad.objects.get_or_create(salad_name=salad_name)
        
        update_salad = reverse('Update_Salad_Page', args=[Salad.objects.first().id])

        response = self.client.get(update_salad)
        assert_that(response.status_code, equal_to(200))

        assert_that(Salad.objects.first().salad_name, equal_to(salad_name))

        self.assertTemplateUsed(response, 'menu/create_salad.html')

    def test_update_salad_post(self):
        salad_name= "name salad"
        Salad.objects.get_or_create(salad_name=salad_name)

        assert_that(Salad.objects.count(), equal_to(1))
        assert_that(Salad.objects.first().salad_name, equal_to(salad_name))

        update_salad = reverse('Update_Salad_Page', args=[Salad.objects.first().id])

        update_name = "updated_salad"
        response = self.client.post(update_salad, {'salad_name': update_name})

        assert_that(response.status_code, equal_to(302))
        assert_that(Salad.objects.count(), equal_to(1))
        assert_that(Salad.objects.first().salad_name, equal_to(update_name))

    def test_update_dessert_get(self):
        dessert_name= "name dessert"
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])
        
        update_dessert = reverse('Update_Dessert_Page', args=[Dessert.objects.first().id])

        response = self.client.get(update_dessert)
        assert_that(response.status_code, equal_to(200))

        assert_that(Dessert.objects.first().dessert_name, equal_to(dessert_name))
        assert_that(Dessert.objects.first().category, equal_to(MENU_TYPE[1][1]))

        self.assertTemplateUsed(response, 'menu/create_dessert.html')


    def test_update_dessert_post(self):
        dessert_name= "name dessert"
        Dessert.objects.get_or_create(dessert_name=dessert_name,
                                      category=MENU_TYPE[1][1])
        
        assert_that(Dessert.objects.count(), equal_to(1))
        assert_that(Dessert.objects.first().dessert_name, equal_to(dessert_name))
        assert_that(Dessert.objects.first().category, equal_to(MENU_TYPE[1][1]))

        updated_dessert_post = reverse('Update_Dessert_Page', args=[Dessert.objects.first().id])

        updated_dessert = "updated name"
        updated_category = MENU_TYPE[0][0]
        response = self.client.post(updated_dessert_post, {'dessert_name': updated_dessert,
                                                     'category': updated_category})

        assert_that(response.status_code, equal_to(302))

        assert_that(Dessert.objects.first().dessert_name, equal_to(updated_dessert))
        assert_that(Dessert.objects.first().category, equal_to(updated_category))

    #DELETE VIEWS

    def test_delete_menu_get(self):
        Menu.objects.get_or_create(day=datetime.now().strftime("%Y-%m-%d"))
        assert_that(Menu.objects.count(), equal_to(1))

        delete_menu = reverse('Delete_menu', args=[Menu.objects.first().id])
        response = self.client.get(delete_menu)
        assert_that(response.status_code, equal_to(200))
        assert_that(Menu.objects.count(), equal_to(1))
        self.assertTemplateUsed(response, 'menu/delete_menu.html')


    def test_delete_menu_post(self):
        Menu.objects.get_or_create(day=datetime.now().strftime("%Y-%m-%d"))
        assert_that(Menu.objects.count(), equal_to(1))

        delete_menu = reverse('Delete_menu', args=[Menu.objects.first().id])
        response = self.client.post(delete_menu)
        assert_that(response.status_code, equal_to(302))
        assert_that(Menu.objects.count(), equal_to(0))

    def test_delete_lunch_get(self):
        Lunch.objects.get_or_create(category=MENU_TYPE[1][1])
        assert_that(Lunch.objects.count(), equal_to(1))

        delete_lunch = reverse('Delete_lunch', args=[Lunch.objects.first().id])
        response = self.client.get(delete_lunch)
        assert_that(response.status_code, equal_to(200))
        assert_that(Lunch.objects.count(), equal_to(1))
        self.assertTemplateUsed(response, 'menu/delete_lunch.html')

    def test_delete_lunch_post(self):
        Lunch.objects.get_or_create(category=MENU_TYPE[1][1])
        assert_that(Lunch.objects.count(), equal_to(1))

        delete_lunch = reverse('Delete_lunch', args=[Lunch.objects.first().id])
        response = self.client.post(delete_lunch)
        assert_that(response.status_code, equal_to(302))
        assert_that(Lunch.objects.count(), equal_to(0))

    def test_delete_meal_get(self):
        Meal.objects.get_or_create(meal_name="meal")
        assert_that(Meal.objects.count(), equal_to(1))

        delete_meal = reverse('Delete_meal', args=[Meal.objects.first().id])
        response = self.client.get(delete_meal)
        assert_that(response.status_code, equal_to(200))
        assert_that(Meal.objects.count(), equal_to(1))
        self.assertTemplateUsed(response, 'menu/delete_meal.html')

    def test_delete_meal_post(self):
        Meal.objects.get_or_create(meal_name="meal")
        assert_that(Meal.objects.count(), equal_to(1))

        delete_meal = reverse('Delete_meal', args=[Meal.objects.first().id])
        response = self.client.post(delete_meal)
        assert_that(response.status_code, equal_to(302))
        assert_that(Meal.objects.count(), equal_to(0))

    def test_delete_salad_get(self):
        Salad.objects.get_or_create(salad_name="salad")
        assert_that(Salad.objects.count(), equal_to(1))

        delete_salad = reverse('Delete_salad', args=[Salad.objects.first().id])
        response = self.client.get(delete_salad)
        assert_that(response.status_code, equal_to(200))
        assert_that(Salad.objects.count(), equal_to(1))
        self.assertTemplateUsed(response, 'menu/delete_salad.html')

    def test_delete_salad_post(self):
        Salad.objects.get_or_create(salad_name="salad")
        assert_that(Salad.objects.count(), equal_to(1))

        delete_salad = reverse('Delete_salad', args=[Salad.objects.first().id])
        response = self.client.post(delete_salad)
        assert_that(response.status_code, equal_to(302))
        assert_that(Salad.objects.count(), equal_to(0))

    def test_delete_dessert_get(self):
        Dessert.objects.get_or_create(dessert_name="salad")
        assert_that(Dessert.objects.count(), equal_to(1))

        delete_dessert = reverse('Delete_dessert', args=[Dessert.objects.first().id])
        response = self.client.get(delete_dessert)
        assert_that(response.status_code, equal_to(200))
        assert_that(Dessert.objects.count(), equal_to(1))
        self.assertTemplateUsed(response, 'menu/delete_dessert.html')

    def test_delete_dessert_post(self):
        Dessert.objects.get_or_create(dessert_name="salad")
        assert_that(Dessert.objects.count(), equal_to(1))

        delete_dessert = reverse('Delete_dessert', args=[Dessert.objects.first().id])
        response = self.client.post(delete_dessert)
        assert_that(response.status_code, equal_to(302))
        assert_that(Dessert.objects.count(), equal_to(0))