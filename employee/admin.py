from django.contrib import admin
from . import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class EmployeeAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'department',
                    'mobile',
                    'country',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'name',
                    'department',
                    'mobile',
                    'country',
                    ]
    list_filter = [
                    'country',
                    'state',
                    ]
    search_fields = [
                    'name',
                    'department',
                    'mobile',
                    'country',
                    'addr1',
                    'addr2',
                    'state',
                    'email',
                    ]

admin.site.register(models.employee, EmployeeAdmin)
admin.site.register(models.department)
admin.site.register(models.employee_visit)
admin.site.register(models.inspection)


