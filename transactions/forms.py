from django import forms

from .models import Transaction

TAILWIND_INPUT_CLASSES = (
    'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2.5 '
    'text-sm text-gray-100 placeholder-gray-500 '
    'focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent '
    'transition-colors'
)

TAILWIND_SELECT_CLASSES = (
    'w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-2.5 '
    'text-sm text-gray-100 '
    'focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent '
    'transition-colors'
)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('asset', 'transaction_type', 'quantity', 'unit_price', 'fee', 'operation_date')
        widgets = {
            'asset': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'transaction_type': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'quantity': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: 100',
                'step': '0.01',
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: 25.50',
                'step': '0.01',
            }),
            'fee': forms.NumberInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: 4.90',
                'step': '0.01',
            }),
            'operation_date': forms.DateInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'type': 'date',
            }),
        }
