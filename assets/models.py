from django.db import models


class Asset(models.Model):
    ASSET_TYPE_CHOICES = [
        ('STOCK', 'Ação'),
        ('FII', 'FII'),
        ('ETF', 'ETF'),
        ('INTERNATIONAL', 'Stock Internacional'),
    ]

    CURRENCY_CHOICES = [
        ('BRL', 'Real (BRL)'),
        ('USD', 'Dólar (USD)'),
    ]

    ticker = models.CharField(max_length=20, unique=True, verbose_name='Ticker')
    name = models.CharField(max_length=100, verbose_name='Nome')
    asset_type = models.CharField(
        max_length=15,
        choices=ASSET_TYPE_CHOICES,
        verbose_name='Tipo',
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default='BRL',
        verbose_name='Moeda',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'
        ordering = ['ticker']

    def __str__(self):
        return f'{self.ticker} - {self.name}'
