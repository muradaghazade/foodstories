from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from accounts.models import User
from .forms import RegisterForm, LoginForm, ResetItDown, PasswordResetConfirmForm, ThePasswordChangeForm, UpdateProfileForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordChangeView
from django.core.exceptions import PermissionDenied

# Create your views here.
class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('inventory:recipe-list')

class LoginUserView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class ProfileView(DetailView):
    model = User
    template_name = 'user-profile.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ResetPassword(PasswordResetView):
    form_class = ResetItDown
    template_name = 'forget_password.html'
    success_url = reverse_lazy('accounts:login')
    email_template_name = 'password_reset_email.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name= "reset_password.html" 
    success_url = reverse_lazy('accounts:login')
    form_class = PasswordResetConfirmForm

class ThePasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = ThePasswordChangeForm
    success_url = reverse_lazy('accounts:login')

class EditProfileView(UpdateView):
    model = User
    template_name = 'edit-user.html'
    form_class = UpdateProfileForm
    
    def get_success_url(self):
        return reverse_lazy('accounts:user-profile', kwargs={'pk':self.get_object().id})

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != self.get_object().username:
            raise PermissionDenied
        return super(EditProfileView, self).dispatch(request, *args, **kwargs)

