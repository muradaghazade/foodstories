from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'placeholder': 'Your Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Your Email', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'id': 'subject', 'placeholder': 'Your Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'id': 'message', 'placeholder': 'Your Message', 'class': 'form-control'}),
        }
