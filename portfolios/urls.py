from django.urls import path

from . import views

app_name = 'portfolios'

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]
