from django.contrib import admin

from myblog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at", "views_count")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "content")
    date_hierarchy = "created_at"
    readonly_fields = ("created_at", "views_count")
