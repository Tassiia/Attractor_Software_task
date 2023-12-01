from django.views.generic import ListView

from accounts.models import CustomUser


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'
    context_object_name = 'people'
