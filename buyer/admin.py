from django.contrib import admin
from . import models
# Register your models here.
from import_export.admin import ImportExportModelAdmin

class BuyerAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'buyer_name',
                    'concerned_person_name',
                    'country',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'name',
                    'buyer_name',
                    'concerned_person_name',
                    'country',
                    ]
    list_filter = [
                    'country',
                    ]
    search_fields = [
                    'name',
                    'buyer_name',
                    'concerned_person_name',
                    'concerned_person_mobile',
                    'country',
                    'addr1',
                    'addr2',
                    'state',
                    'email',
                    ]


admin.site.register(models.buyer, BuyerAdmin)
admin.site.register(models.buyer_complaint_categories)
admin.site.register(models.buyer_complaints)
admin.site.register(models.buyer_general_feedback)
admin.site.register(models.buyer_general_feedback_categories)
admin.site.register(models.complaint_response)