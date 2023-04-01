from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('menu_name','text', 'url', 'parent')
    fields = ('menu_name','text', 'url', 'parent')

admin.site.register(Item, ItemAdmin)
# Register your models here.
