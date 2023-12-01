from django.urls import path

from accounts.views import RegistrationView, UsernameChangeView, UsersListView, UserDetailedView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register_user'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/<int:pk>/', UserDetailedView.as_view(), name='user_detailed'),
    path('users/<int:pk>/change-username/', UsernameChangeView.as_view(), name='change_username'),

]
