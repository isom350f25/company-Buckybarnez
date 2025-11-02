from django.contrib import admin
from .models import employee



@admin.register(employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','phone_number', 'position', 'joined_on')
    search_fields = ('name', 'position')
    list_filter = ('joined_on',)
    
    
    

# Register your models here.
