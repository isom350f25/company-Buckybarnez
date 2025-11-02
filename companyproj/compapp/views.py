from django.shortcuts import render
from .models import employee
 
def employee_list_view(request):
    employees = employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})
