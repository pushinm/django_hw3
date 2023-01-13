from django.shortcuts import render
from .models import Employee, Logins
# Create your views here.

def employee(request):
    template_ = 'employee_list.html'
    employee = Employee.objects.all()

    context = {
        'employee': employee
    }
    return render(request, template_, context=context)

def logins(request):
    template_ = 'logins.html'
    logins = Logins.objects.all()

    context = {
        'logins': logins
    }

    return render(request, template_, context=context)