from django import forms
from .models import ContactUs, Recipe

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

class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'text', 'picture', 'category', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'id': 'title', 'placeholder': 'Title', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'id': 'description', 'placeholder': 'Description', 'class': 'form-control'}),
            'text': forms.Textarea(attrs={'id': 'text', 'placeholder': 'Text', 'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'id': 'picture', 'placeholder': 'Picture', 'class': 'form-control'}),
            'category': forms.Select(attrs={'id': 'category', 'placeholder': 'Category', 'class': 'form-control'}),
            'author': forms.Select(attrs={'id': 'author', 'placeholder': 'Author', 'class': 'form-control'}),
        }
