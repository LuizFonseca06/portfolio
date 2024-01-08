from django.contrib import admin
from .models import Job

# Define a custom admin class
class JobAdmin(admin.ModelAdmin):
    list_display = ('summary',)  # Add other fields if needed

# Register the Job model with the custom admin class
admin.site.register(Job, JobAdmin)
