from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='public/landing.html'), name='landing'),
    path('', include('accounts.urls')),
    path('ativos/', include('assests.urls')),
    path('transacoes/', include('transations.urls')),
    path('', include('portfolios.urls')),
]
