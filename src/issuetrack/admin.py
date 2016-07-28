from django.contrib import admin
from .models import Issue,Tag,Comment

# Register your models here.

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
	list_display = ['title' ,'office','application_no','applicant_name','birth_date','license_no','issue_description','project','creator','owner','created','closed']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass


