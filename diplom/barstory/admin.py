from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ClassicCocktails, Profile


class ClassicAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ('title',)
    list_display = ('title', 'get_photo')

    def get_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width='50' >")

    get_photo.short_description = 'Фото коктейлей'


admin.site.register(ClassicCocktails, ClassicAdmin)
admin.site.register(Profile)

admin.site.site_header = "BarStory Админпанель"
admin.site.site_title = "BarStory Admin"
