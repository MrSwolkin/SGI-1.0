from django.contrib import admin

from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'name', 'asset_type', 'currency', 'created_at')
    search_fields = ('ticker', 'name')
    list_filter = ('asset_type', 'currency')
