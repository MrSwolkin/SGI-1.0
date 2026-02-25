from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserCreationForm, EmailAuthenticationForm


class LandingPageView(TemplateView):
    template_name = 'public/landing.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('portfolios:dashboard')
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Conta criada com sucesso! Faça login para continuar.')
        return response


class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
