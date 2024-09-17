from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'employees/update_employee.html', {'form': form})

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('home')

    return render(request, 'employees/delete_employee.html', {'employee': employee})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


