from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name-field',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email-field',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'subject-field',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'id': 'message-field',
            }),
        }