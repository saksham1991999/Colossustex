from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin

class AgentAdmin(ImportExportModelAdmin):
    list_display = [
                    'name',
                    'country',
                    ]
    # list_editable = [
    #                 'value',
    #                 ]
    list_display_links =[
                    'name',
                    'country',
                    ]
    list_filter = [
                    'country',
                    ]
    search_fields = [
                    'name',
                    'country',
                    'addr1',
                    'addr2',
                    'state',
                    'email',
                    ]



admin.site.register(models.agent, AgentAdmin)
admin.site.register(models.agent_complaint_categories)
admin.site.register(models.agent_complaints)
admin.site.register(models.agent_general_feedback_categories)
admin.site.register(models.agent_general_feedback)
admin.site.register(models.complaint_response)