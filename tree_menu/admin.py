from django.contrib import admin
from django.contrib.admin import ModelAdmin

from tree_menu.models import Menu


@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    list_display = ('title', 'parent_menu', 'is_active',)
    list_filter = ('is_active', )
    search_fields = ('title', )

