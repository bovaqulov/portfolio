from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


class GalleriyaInline(admin.TabularInline):

    fk_name = 'project'
    model = Gallery
    extra = 1


@admin.register(Projects)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('pk', 'title', 'price', 'created_at', 'category', 'get_photo')
    list_editable = ('title', 'price', 'category',)
    inlines = [GalleriyaInline]

    def get_photo(self, obj):

        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
            except:
                return '-'
        return '-'


admin.site.register(UsersALL)