from django.contrib import admin
from .models import Issue, Citizen

# Register your models here.
admin.site.register(Citizen)

class IssueAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'description', 'votes', 'created_date', 'allow_comments']

admin.site.register(Issue, IssueAdmin)
