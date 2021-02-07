from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee_hub, name='employee_hub'),
    path('create/employee', views.create_employee, name='create_employee'),
    path('update/employee/<uuid:employee_uuid>', views.update_employee, name='update_employee'),
    path('delete/employee/<uuid:employee_uuid>', views.delete_employee, name='delete_employee'),
]