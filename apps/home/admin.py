from django.contrib import admin

from . import models

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'downloads', 'size', 'display_genres', 'added_at', 'current_price']
    list_display_links = ['id', 'name']
    list_filter = ['genre', 'added_at', 'current_price']
    search_fields = ['name', 'tags__name', 'studio__name']


    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genre.all()])

    display_genres.short_description = 'Жанры'



class LibraryItemInline(admin.TabularInline):
    model = models.GameLibraryItem
    extra = 1


class LibraryAdmin(admin.ModelAdmin):
    inlines = [LibraryItemInline]


class WishLib(admin.TabularInline):
    model = models.WishLibraryItem
    extra = 1


class WishLIB(admin.ModelAdmin):
    inlines = [WishLib]

admin.site.register(models.GameLibrary, LibraryAdmin)
admin.site.register(models.WishLibrary, WishLIB)
admin.site.register(models.Game,GameAdmin)
admin.site.register(models.Genre,GenreAdmin)
admin.site.register(models.Tags)
admin.site.register(models.Studio)