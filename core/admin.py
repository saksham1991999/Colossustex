from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = 'Colossustex'


#COMMON MODELS
admin.site.register(models.User)
admin.site.register(models.office)
admin.site.register(models.to_do)
admin.site.register(models.note)
admin.site.register(models.updates)
admin.site.register(models.notifications)
admin.site.register(models.suplus_product)

#PRODUCT MODELS
admin.site.register(models.category)
admin.site.register(models.subcategory1)
admin.site.register(models.subcategory2)
admin.site.register(models.product_shade)
admin.site.register(models.intermingle)
admin.site.register(models.required_no_of_nips)
admin.site.register(models.product)

#INQUIRY MODELS
admin.site.register(models.inquiry)
admin.site.register(models.inquiry_product)
admin.site.register(models.notified_suppliers)
admin.site.register(models.supplier_quotations)
admin.site.register(models.forwarded_quotation)
admin.site.register(models.inquiry_update)



admin.site.register(models.order)
admin.site.register(models.payment)
admin.site.register(models.shipment)
admin.site.register(models.bill)




