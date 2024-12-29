from django.contrib import admin
from .models import Dashboard , ReferenceBook , Keyword, Imam, Catalogue , Index 
from django.urls import path


# Register your models here.
@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ("page", "language", "title")
    list_filter = ("page", "language")
    search_fields = ("title", "content")


class KeywordAdmin(admin.ModelAdmin):
    list_display = ("name_english", "name_urdu")
    search_fields = ("name_english", "name_urdu")
    filter_horizontal = ("reference_books",)  # Multi-select for associating reference books with keywords

class ReferenceBookAdmin(admin.ModelAdmin):
    list_display = ("name_english", "name_urdu")
    search_fields = ("name_english", "name_urdu")
    filter_horizontal = ("keywords",)  # Multi-select for associating keywords with reference books

@admin.register(Imam)
class ImamAdmin(admin.ModelAdmin):
    list_display = ('name_english', 'name_urdu')
    
@admin.register(Catalogue)
class CatalogueAdmin(admin.ModelAdmin):
    list_display = ("title_english", "title_urdu", "reference_book", "keyword", "imam")
    search_fields = ("title_english", "title_urdu", "reference_book__name_english", "keyword__name_english", "imam__name_english")
    list_filter = ("reference_book", "keyword", "imam")
    
    # Fields displayed in the form for adding/editing a Catalogue entry
    fields = ("title_english", "title_urdu", "reference_book", "keyword", "imam", "description_english", "description_urdu")


class IndexAdmin(admin.ModelAdmin):
    list_display = ("keyword", "english_search_count", "urdu_search_count", "created_at")
    search_fields = ("keyword__name_english", "keyword__name_urdu")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)

admin.site.register(Index, IndexAdmin)

admin.site.register(ReferenceBook, ReferenceBookAdmin)
admin.site.register(Keyword, KeywordAdmin)

# admin.site.register(AnalyticsFilter)