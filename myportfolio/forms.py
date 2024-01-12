from django import forms
from .models import UsersALL


class ContactForm(forms.ModelForm):
    class Meta:
        model = UsersALL
        fields = ['name', 'tel', "message"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ism'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqam'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Xabar',
            })
        }