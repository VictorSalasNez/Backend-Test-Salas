from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def employee_hub(request):
    return render(request, 'employees/menu.html', {'employees'  : Employee.objects.all() })


# CREATE VIEWS
def create_employee(request):
    # TODO send a popup message if fail or success
    # TODO block two menus for the same day
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = {'employeeform': EmployeeForm()}
    return render(request, 'employees/create_employee.html', form) 


# UPDATE VIEWS
def update_employee(request, employee_uuid):
    menu = Employee.objects.get(uuid=employee_uuid)
    form = EmployeeForm(instance=menu)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect(employee_hub)

    menu_form = {'employeeform': form}
    return render(request, 'employees/create_employee.html', menu_form)

# DELETE VIEWS
def delete_employee(request, employee_uuid):
    menu = Employee.objects.get(uuid=employee_uuid)
    if request.method == 'POST':
        menu.delete()
        return redirect(employee_hub)

    form = {'item': menu}
    return render(request, "employees/delete_employee.html", form)