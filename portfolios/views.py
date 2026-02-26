import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from portfolios.services import get_portfolio_summary, get_composition_by_type


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'portfolios/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        summary = get_portfolio_summary(user)
        composition = get_composition_by_type(user)

        context['total_invested'] = summary['total_invested']
        context['positions'] = summary['positions']
        context['num_assets'] = summary['num_assets']
        context['largest_position'] = summary['largest_position']
        context['last_transaction'] = summary['last_transaction']
        context['composition'] = composition

        chart_labels = [item['type'] for item in composition]
        chart_data = [float(item['percentage']) for item in composition]
        context['chart_labels'] = json.dumps(chart_labels)
        context['chart_data'] = json.dumps(chart_data)

        return context
