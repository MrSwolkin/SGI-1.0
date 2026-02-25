from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class TransactionListView(LoginRequiredMixin, TemplateView):
    template_name = 'transactions/transaction_list.html'
