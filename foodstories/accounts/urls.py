from django.urls import path
from django.contrib.auth.views import LogoutView

from accounts.views import RegisterView, LoginUserView, ProfileView, CustomPasswordResetConfirmView, ResetPassword

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user-profile/<int:pk>', ProfileView.as_view(), name='user-profile'),
    path('log-out', LogoutView.as_view(), name='log-out'),
    path('reset-password', ResetPassword.as_view(), name='reset-password'),

    path('password-reset-confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name = 'password-reset-confirm'),
]