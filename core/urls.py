from django.contrib import admin
from django.urls import include, path

from accounts.views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing'),
    path('', include('accounts.urls')),
    path('ativos/', include('assets.urls')),
    path('transacoes/', include('transactions.urls')),
    path('', include('portfolios.urls')),
]
