from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import AddUserView, UsernameChangeView, UsersListView, UserDeleteView

app_name = 'accounts'

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/add/', AddUserView.as_view(), name='register_user'),
    path('users/<int:pk>/change-username/', UsernameChangeView.as_view(), name='change_username'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),

    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
