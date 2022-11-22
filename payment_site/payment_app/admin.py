from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_descrip', 'price')

    def short_descrip(self, obj):
        result = f'{obj.description[:20]}...'
        return result

    short_descrip.short_description = 'Краткое описание'
