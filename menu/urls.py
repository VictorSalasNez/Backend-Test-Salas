from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_hub, name='menu_hub'),
    path('<uuid:menu_uuid>', views.menus_day, name='Nora_Menu'),
    
    path('create/lunch', views.create_lunch, name='Create_Lunch_Page'),
    path('create/menu', views.create_menu, name='Create_Menu_Page'),
    path('create/meal', views.create_meal, name='Create_Meal_Page'),
    path('create/salad', views.create_salad, name='Create_Salad_Page'),
    path('create/dessert', views.create_dessert, name='Create_Dessert_Page'),

    path('update/lunch/<int:pk>', views.update_lunch, name='Update_Lunch_Page'),
    path('update/menu/<int:pk>', views.update_menu, name='Update_Menu_Page'),
    path('update/meal/<int:pk>', views.update_meal, name='Update_Meal_Page'),
    path('update/salad/<int:pk>', views.update_salad, name='Update_Salad_Page'),
    path('update/dessert/<int:pk>', views.update_dessert, name='Update_Dessert_Page'),

    path('delete/lunch/<int:pk>', views.delete_lunch, name='Delete_lunch'),
    path('delete/menu/<int:pk>', views.delete_menu, name='Delete_menu'),
    path('delete/meal/<int:pk>', views.delete_meal, name='Delete_meal'),
    path('delete/salad/<int:pk>', views.delete_salad, name='Delete_salad'),
    path('delete/dessert/<int:pk>', views.delete_dessert, name='Delete_dessert'),
    
    path('send_message/<int:menu_id>', views.send_message, name='Send_Message'),
    
]