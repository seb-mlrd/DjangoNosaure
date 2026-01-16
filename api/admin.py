from django.contrib import admin
from django.utils.html import format_html
from . import models


class DinoAdmin(admin.ModelAdmin):
    list_display = ['name', 'taille', 'poid', 'display_photo']  # Champs à afficher dans la liste des articles
    search_fields = ['name', 'description'] # Champs à rechercher
    list_per_page = 25  # Nombre d'articles par page dans la liste des articles
    
    def display_photo(self, obj):
        if obj.image:
            return format_html('<a href="{}"><img src="{}" style="max-height: 50px; max-width: 50px;" /></a>', obj.image.url, obj.image.url)
        return None

admin.site.register(models.Dinosaur, DinoAdmin)
admin.site.register(models.Localisation)
admin.site.register(models.Periode)
admin.site.register(models.Alimentation)
admin.site.register(models.Category)
