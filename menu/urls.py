from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_hub, name='menu_hub'),
    path('<uuid:menu_uuid>/', views.menus_day, name='Nora_Menu'),
    path('create/lunch', views.create_lunch, name='Create_Lunch_Page'),
    path('create/menu', views.create_menu, name='Create_Menu_Page'),
    path('send_message/<int:menu_id>', views.send_message, name='Send_Message'),
    
]