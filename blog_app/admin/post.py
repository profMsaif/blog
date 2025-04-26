from django.contrib import admin

from blog_app import models


class PostCommentInline(admin.TabularInline):
    model = models.Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_on")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostCommentInline]


def register_post_admin():
    admin.site.register(models.Post, PostAdmin)
