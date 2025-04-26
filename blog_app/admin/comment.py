from django.contrib import admin

from blog_app import models


class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "body", "active", "created_on")
    search_fields = ["name"]


def register_comment_admin():
    admin.site.register(models.Comment, CommentAdmin)
