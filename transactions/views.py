from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from assets.models import Asset
from .forms import TransactionForm
from .models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        qs = Transaction.objects.filter(user=self.request.user).select_related('asset')
        asset_pk = self.request.GET.get('asset')
        if asset_pk:
            qs = qs.filter(asset_id=asset_pk)
        transaction_type = self.request.GET.get('type')
        if transaction_type in ('BUY', 'SELL'):
            qs = qs.filter(transaction_type=transaction_type)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_assets'] = Asset.objects.all().order_by('ticker')
        context['selected_asset'] = self.request.GET.get('asset', '')
        context['selected_type'] = self.request.GET.get('type', '')
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Transação registrada com sucesso!')
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Transação atualizada com sucesso!')
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Transação excluída com sucesso!')
        return super().form_valid(form)
