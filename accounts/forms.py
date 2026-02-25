from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import CustomUser

TAILWIND_INPUT_CLASSES = (
    'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2.5 '
    'text-sm text-gray-100 placeholder-gray-500 '
    'focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent '
    'transition-colors'
)


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Seu nome',
        }),
    )
    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Seu sobrenome',
        }),
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'seu@email.com',
        }),
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Crie uma senha',
        }),
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Repita a senha',
        }),
    )

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe uma conta com este email.')
        return email


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'seu@email.com',
            'autofocus': True,
        }),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': TAILWIND_INPUT_CLASSES,
            'placeholder': 'Sua senha',
        }),
    )
