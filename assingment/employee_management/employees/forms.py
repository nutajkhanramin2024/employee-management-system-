from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
