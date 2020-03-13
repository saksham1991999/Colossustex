from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = 'Colossustex'



admin.site.register(models.User)
admin.site.register(models.category)
admin.site.register(models.subcategory1)
admin.site.register(models.subcategory2)
admin.site.register(models.product_shade)
admin.site.register(models.intermingle)
admin.site.register(models.required_no_of_nips)
admin.site.register(models.product)
admin.site.register(models.office)
admin.site.register(models.order)
admin.site.register(models.payment)
admin.site.register(models.shipment)
admin.site.register(models.bill)

admin.site.register(models.to_do)
admin.site.register(models.note)
admin.site.register(models.event)
admin.site.register(models.notifications)
admin.site.register(models.suplus_product)
