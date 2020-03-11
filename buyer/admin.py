from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.buyer)
admin.site.register(models.sample_request)
admin.site.register(models.sample_follow_up)
admin.site.register(models.buyer_complaint_categories)
admin.site.register(models.buyer_complaints)
admin.site.register(models.buyer_general_feedback)
admin.site.register(models.buyer_general_feedback_categories)
admin.site.register(models.complaint_response)