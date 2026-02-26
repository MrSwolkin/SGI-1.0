from django.urls import path

from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='list'),
    path('nova/', views.TransactionCreateView.as_view(), name='create'),
    path('editar/<int:pk>/', views.TransactionUpdateView.as_view(), name='update'),
    path('excluir/<int:pk>/', views.TransactionDeleteView.as_view(), name='delete'),
]
