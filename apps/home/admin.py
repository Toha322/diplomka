from django.contrib import admin

from . import models

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'downloads', 'size', 'genre', 'added_at','current_price']
    list_display_links = ['id', 'name']
    list_editable = ['genre']
    list_filter = ['genre', 'added_at','current_price']

admin.site.register(models.Game,GameAdmin)
admin.site.register(models.Genre,GenreAdmin)
admin.site.register(models.Tags)
admin.site.register(models.Studio)