from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = 'Colossustex'

admin.site.register(models.product)
admin.site.register(models.office)
admin.site.register(models.order)
admin.site.register(models.payment)
admin.site.register(models.shipment)
admin.site.register(models.bill)
admin.site.register(models.User)
admin.site.register(models.to_do)
