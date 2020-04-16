from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class SupplierAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'concerned_person_name',
                    'country',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'name',
                    'concerned_person_name',
                    'country',
                    ]
    list_filter = [
                    'country',
                    'products',
                    ]
    search_fields = [
                    'name',
                    'concerned_person_name',
                    'concerned_person_mobile',
                    'country',
                    'addr1',
                    'addr2',
                    'state',
                    'email',
                    'products',
                    ]


admin.site.register(models.supplier, SupplierAdmin)
admin.site.register(models.supplierquotation)
admin.site.register(models.supplier_feedback_categories)
admin.site.register(models.supplier_feedback)
admin.site.register(models.supplier_complaint_categories)
admin.site.register(models.supplier_complaints)
admin.site.register(models.complaint_response)