from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.agent)
admin.site.register(models.agent_complaint_categories)
admin.site.register(models.agent_complaints)
admin.site.register(models.agent_general_feedback_categories)
admin.site.register(models.agent_general_feedback)
admin.site.register(models.complaint_response)