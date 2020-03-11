from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.supplier)
admin.site.register(models.supplierquotation)
admin.site.register(models.supplier_feedback_categories)
admin.site.register(models.supplier_feedback)
admin.site.register(models.supplier_complaint_categories)
admin.site.register(models.supplier_complaints)
admin.site.register(models.complaint_response)