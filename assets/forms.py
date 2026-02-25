from django import forms

from .models import Asset

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


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ('ticker', 'name', 'asset_type', 'currency')
        widgets = {
            'ticker': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: PETR4',
            }),
            'name': forms.TextInput(attrs={
                'class': TAILWIND_INPUT_CLASSES,
                'placeholder': 'Ex: Petrobras PN',
            }),
            'asset_type': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
            'currency': forms.Select(attrs={
                'class': TAILWIND_SELECT_CLASSES,
            }),
        }
