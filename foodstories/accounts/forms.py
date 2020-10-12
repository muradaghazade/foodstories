from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Confirm password',
                'class' : 'form-control',
             }))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'id': 'first_name', 'placeholder': 'Your First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'id': 'last_name', 'placeholder': 'Your Last Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'id': 'username', 'placeholder': 'Your Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email', 'class': 'form-control'}),
        }

class LoginForm(AuthenticationForm):
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Password',
                'class' : 'form-control',
            }))

    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'id': 'username',
                'placeholder': 'Your Username',
                'class': 'form-control'
            }))

    class Meta:
        model = User
        fields = ['username', 'password']

class ResetItDown(PasswordResetForm):
    email = forms.EmailField(
        widget = forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form-control',
        })
    )

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
             }))
    
    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-control',
             }))

    class Meta:
        fields = ("new_password1", 'new_password2', )

class ThePasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Old password',
                'class' : 'form-control',
            }))

    new_password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'New password',
                'class' : 'form-control',
            }))

    new_password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'placeholder' : 'Re-enter new password',
                'class' : 'form-control',
            }))

    class Meta:
        fields = ("old_password", 'new_password1', 'new_password2', )