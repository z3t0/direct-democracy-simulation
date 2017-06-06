from django.contrib import admin
from .models import Issue, Citizen, Comment

# Register your models here.
admin.site.register(Citizen)
admin.site.register(Comment)


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class IssueAdmin(admin.ModelAdmin):
    fields = ['author', 'title', 'description', 'votes', 'created_date']

    inlines = [CommentInline]


admin.site.register(Issue, IssueAdmin)
