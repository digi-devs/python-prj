from django.contrib import admin
from EmpAPI.models import Employee,Roles,Department

# Register your models here.

admin.site.register(Employee)
admin.site.register(Roles)
admin.site.register(Department)