from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('asset', 'transaction_type', 'quantity', 'unit_price', 'fee', 'operation_date', 'user')
    search_fields = ('asset__ticker', 'asset__name')
    list_filter = ('transaction_type', 'asset__asset_type', 'operation_date')
