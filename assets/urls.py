from django.urls import path

from . import views

app_name = 'assets'

urlpatterns = [
    path('', views.AssetListView.as_view(), name='list'),
    path('novo/', views.AssetCreateView.as_view(), name='create'),
]
