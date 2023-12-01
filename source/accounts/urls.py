from django.urls import path

from accounts.views import RegistrationView, UsernameChangeView


app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_user'),
    path('user/<int:pk>/change-username/', UsernameChangeView.as_view(), name='change_username'),
]
