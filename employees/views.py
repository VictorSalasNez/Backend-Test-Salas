from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="Login_page")
def employee_hub(request):
    return render(request, 'employees/menu.html', {'employees'  : Employee.objects.all() })


# CREATE VIEWS
@login_required(login_url="Login_page")
def create_employee(request):
    # TODO send a popup message if fail or success
    # TODO block two menus for the same day
    employe_form = EmployeeForm()
    if request.method == 'POST':
        employe_form = EmployeeForm(request.POST)
        if employe_form.is_valid():
            employe_form.save()
    form = {'employeeform': employe_form}
    return render(request, 'employees/create_employee.html', form) 

# UPDATE VIEWS
@login_required(login_url="Login_page")
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
@login_required(login_url="Login_page")
def delete_employee(request, employee_uuid):
    menu = Employee.objects.get(uuid=employee_uuid)
    if request.method == 'POST':
        menu.delete()
        return redirect(employee_hub)

    form = {'item': menu}
    return render(request, "employees/delete_employee.html", form)