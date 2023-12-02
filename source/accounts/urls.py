from django.urls import path

from accounts.views import AddUserView, UsernameChangeView, UsersListView, UserDetailedView, UserDeleteView

app_name = 'accounts'

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('users/add/', AddUserView.as_view(), name='register_user'),
    path('users/<int:pk>/', UserDetailedView.as_view(), name='user_detailed'),
    path('users/<int:pk>/change-username/', UsernameChangeView.as_view(), name='change_username'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]
