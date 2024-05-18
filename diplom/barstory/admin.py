from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import ClassicCocktails, Profile, History, Events, News


class EventAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())
    event_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Events
        fields = '__all__'


class EventsAdmin(admin.ModelAdmin):
    form = EventAdminForm
    list_per_page = 10
    search_fields = ('title',)
    list_display = ('title', 'event_photo')

    def get_photo(self, objects):
        if objects.event_photo:
            return mark_safe(f"<img src='{objects.event_photo.url}' width='50' >")


class NewsAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())
    news_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_per_page = 10
    search_fields = ('title',)
    list_display = ('title', 'new_photo')

    def get_photo(self, objects):
        if objects.new_photo:
            return mark_safe(f"<img src='{objects.new_photo.url}' width='50' >")


class CoctailAdminForm(forms.ModelForm):
    recept = forms.CharField(widget=CKEditorUploadingWidget())
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ClassicCocktails
        fields = '__all__'


class ClassicCoctailsAdmin(admin.ModelAdmin):
    form = CoctailAdminForm
    list_per_page = 10
    search_fields = ('title',)
    list_display = ('title', 'get_photo')

    def get_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src='{objects.photo.url}' width='50' >")

    get_photo.short_description = 'Фото коктейлей'


class HistoryAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorUploadingWidget())
    short_text = forms.CharField(widget=CKEditorUploadingWidget())
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = History
        fields = '__all__'


class HistoryAdmin(admin.ModelAdmin):
    form = HistoryAdminForm
    list_display = ('title', 'get_photo')

    def get_photo(self, objects):
        if objects.history_photo:
            return mark_safe(f"<img src='{objects.history_photo.url}' width='50' >")


admin.site.register(ClassicCocktails, ClassicCoctailsAdmin)
admin.site.register(Profile)
admin.site.register(News, NewsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(History, HistoryAdmin)

admin.site.site_header = "BarStory Админпанель"
admin.site.site_title = "BarStory Admin"
