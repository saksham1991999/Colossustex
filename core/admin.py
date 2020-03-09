from django.contrib import admin
from . import models
# Register your models here.

admin.site.site_header = 'Colossustex'

admin.site.register(models.product)
admin.site.register(models.supplier)
admin.site.register(models.customer)
admin.site.register(models.agent)
admin.site.register(models.office)
admin.site.register(models.employee)
admin.site.register(models.order)
admin.site.register(models.supplierquotation)
admin.site.register(models.payment)
admin.site.register(models.shipment)
admin.site.register(models.customerfeedback)
admin.site.register(models.User)
