from django.contrib import admin
from .models import SearchHistory

@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'temperature', 'searched_at')
    search_fields = ('city_name',)
