from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_hub, name='menu_hub'),
    path('<uuid:menu_uuid>/', views.menus_day, name='Nora_Menu'),
    path('create/', views.create, name='Create_Page'),
    
]