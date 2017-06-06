from django.contrib import admin
from .models import Issue, Citizen, Comment

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Issue)
admin.site.register(Comment)
