
from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('', views.dashboard, name='Noras Dasboard'),
    path('register/', views.register, name='Register_page'),
    path('login/', views.login_page, name='Login_page'),
    path('logout/', views.logout_page, name='Logout_page'),
]

