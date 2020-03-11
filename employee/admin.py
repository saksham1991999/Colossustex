from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.employee)
admin.site.register(models.department)
admin.site.register(models.employee_visit)
admin.site.register(models.inspection)