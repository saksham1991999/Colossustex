from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.site_header = 'Colossustex'

class OfficeAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'contact_person',
                    'mobile',
                    ]
    list_display_links =[
                    'name',
                    'contact_person',
                    ]
    list_filter = [
                    'state',
                    'country',
                    ]
    search_fields = [
                    'name',
                    'contact_person',
                    'addr1',
                    'addr2',
                    'state',
                    ]

class PaymentTermAdmin(ImportExportModelAdmin):
    list_display = [
                    'term',
                    'days',
                    ]
    list_display_links =[
                    'term',
                    'days',
                    ]
    list_filter = [
                    'term',
                    'days',
                    ]
    search_fields = [
                    'term',
                    'days',
                    ]

class CategoryAdmin(ImportExportModelAdmin):
    list_display = [
                    'title',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'title',
                    ]
    list_filter = [
                    'title',
                    ]
    search_fields = [
                    'title',
                    ]

class SubCategory1Admin(ImportExportModelAdmin):
    list_display = [
                    'title',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'title',
                    ]
    list_filter = [
                    'title',
                    ]
    search_fields = [
                    'title',
                    ]

class SubCategory2Admin(ImportExportModelAdmin):
    list_display = [
                    'title',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'title',
                    ]
    list_filter = [
                    'title',
                    ]
    search_fields = [
                    'title',
                    ]

class ProductShadeAdmin(ImportExportModelAdmin):
    list_display = [
                    'shade_name',
                    'shade_code',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'shade_name',
                    'shade_code',
                    ]
    list_filter = [
                    'shade_name',
                    'shade_code',
                    ]
    search_fields = [
                    'shade_name',
                    'shade_code',
                    ]

class IntermingleAdmin(ImportExportModelAdmin):
    list_display = [
                    'title',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'title',
                    ]
    list_filter = [
                    'title',
                    ]
    search_fields = [
                    'title',
                    ]

class RequiredNoOfNipsAdmin(ImportExportModelAdmin):
    list_display = [
                    'title',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'title',
                    ]
    list_filter = [
                    'title',
                    ]
    search_fields = [
                    'title',
                    ]

class ProductAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'category',
                    'sub_category_1',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'name',
                    'category',
                    'sub_category_1',
                    ]
    list_filter = [
                    'application',
                    'polymer_fiber',
                    'luster',
                    'filament_cross_section',
                    'intermingle',
                    'required_no_of_nips',
                    'lycra_percent_or_any_additional_additive',
                    'shade',
                    ]
    search_fields = [
                    'additional_info',
                    'remarks',
                    'application',
                    'polymer_fiber',
                    'luster',
                    'filament_cross_section',
                    'intermingle',
                    'required_no_of_nips',
                    'lycra_percent_or_any_additional_additive',
                    'shade',
                    'name',
                    'category',
                    'sub_category_1',
                    ]

class InquiryAdmin(ImportExportModelAdmin):
    list_display = [
                    'buyer',
                    'source',
                    'status',
                    'received_datetime',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'buyer',
                    'source',
                    'status',
                    'received_datetime',
                    ]
    list_filter = [
                    'buyer',
                    'source',
                    'status',
                    'close_choice',
                    'inquiry_user',
                    'agent',
                    ]
    search_fields = [
                    'buyer',
                    'source',
                    'status',
                    'close_choice',
                    'inquiry_user',
                    'agent',
                    'remarks',
                    ]

class InquiryProductAdmin(ImportExportModelAdmin):
    list_display = [
                    'inquiry',
                    'product',
                    'qty',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'inquiry',
                    'product',
                    'qty',
                    ]
    list_filter = [
                    'inco_terms',
                    'payment_terms',
                    'packing_requirement',
                    'destination_port',
                    ]
    search_fields = [
                    'inquiry',
                    'product',
                    'qty',
                    'inco_terms',
                    'payment_terms',
                    'packing_requirement',
                    'destination_port',
                    ]

class SupplierQuotationsAdmin(ImportExportModelAdmin):
    list_display = [
                    'inquiry',
                    'supplier',
                    'product',
                    'price_kg',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'inquiry',
                    'supplier',
                    'product',
                    'price_kg',
                    ]
    list_filter = [
                    'supplier',
                    'product',
                    'payment_terms',
                    ]
    search_fields = [
                    'inquiry',
                    'supplier',
                    'product',
                    'price_kg',
                    'payment_terms',
                    ]

class ForwardedQuotationsAdmin(ImportExportModelAdmin):
    list_display = [
                    'inquiry',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'inquiry',
                    ]
    list_filter = [
                    'inquiry',
                    ]
    search_fields = [
                    'inquiry',
                    ]

class InquiryUpdatesAdmin(ImportExportModelAdmin):
    list_display = [
                    'inquiry',
                    'employee',
                    'update_date_time',
                    'subject',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links = [
                    'inquiry',
                    'employee',
                    'update_date_time',
                    'subject',
                    ]
    list_filter = [
                    'employee',
                    'subject',
                    ]
    search_fields = [
                    'inquiry',
                    'employee',
                    'update_date_time',
                    'subject',
                    'content',
                    ]


#COMMON MODELS
admin.site.register(models.User)
admin.site.register(models.office, OfficeAdmin)
admin.site.register(models.to_do)
admin.site.register(models.note)
admin.site.register(models.updates)
admin.site.register(models.notifications)
admin.site.register(models.suplus_product)
admin.site.register(models.PaymentTerms, PaymentTermAdmin)


# PRODUCT MODELS
admin.site.register(models.category, CategoryAdmin)
admin.site.register(models.subcategory1, SubCategory1Admin)
admin.site.register(models.subcategory2, SubCategory2Admin)
admin.site.register(models.product_shade, ProductShadeAdmin)
admin.site.register(models.intermingle, IntermingleAdmin)
admin.site.register(models.required_no_of_nips, RequiredNoOfNipsAdmin)
admin.site.register(models.product, ProductAdmin)

# INQUIRY MODELS
admin.site.register(models.inquiry, InquiryAdmin)
admin.site.register(models.inquiry_product, InquiryProductAdmin)
admin.site.register(models.supplier_quotations, SupplierQuotationsAdmin)
admin.site.register(models.forwarded_quotation, ForwardedQuotationsAdmin)
admin.site.register(models.inquiry_update, InquiryUpdatesAdmin)

# SAMPLE REQUESTS
admin.site.register(models.SampleRequest)
admin.site.register(models.SampleRequestProduct)
admin.site.register(models.CustomerSampleRef)
admin.site.register(models.SampleRequestDispatch)
admin.site.register(models.SampleRequestFeedback)

# INDENT MODELS
admin.site.register(models.Indent)
admin.site.register(models.IndentProduct)



