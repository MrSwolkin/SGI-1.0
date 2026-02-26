from django.conf import settings
from django.db import models

from assets.models import Asset


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('BUY', 'Compra'),
        ('SELL', 'Venda'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions',
        verbose_name='Usuário',
    )
    asset = models.ForeignKey(
        Asset,
        on_delete=models.PROTECT,
        related_name='transactions',
        verbose_name='Ativo',
    )
    transaction_type = models.CharField(
        max_length=4,
        choices=TRANSACTION_TYPE_CHOICES,
        verbose_name='Tipo',
    )
    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Quantidade',
    )
    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        verbose_name='Preço Unitário',
    )
    fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        verbose_name='Taxa',
    )
    operation_date = models.DateField(verbose_name='Data da Operação')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = 'Transações'
        ordering = ['-operation_date', '-created_at']

    def __str__(self):
        return f'{self.get_transaction_type_display()} - {self.asset.ticker} - {self.operation_date}'

    @property
    def total_value(self):
        return self.quantity * self.unit_price + self.fee
