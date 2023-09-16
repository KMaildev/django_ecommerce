from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)