from django.urls import path
from . import views
from .views import delete_employee, employee_list

urlpatterns = [
    path('', views.home, name='home'),  # Homepage that lists all employees
    path('add/', views.add_employee, name='add_employee'),  # Add employee form
    path('update/<int:id>/', views.update_employee, name='update_employee'),  # Update employee form
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('employees/', employee_list, name='employee_list'),
    path('delete_employee/<int:id>/', delete_employee, name='delete_employee')
    # Delete employee confirmation
]
