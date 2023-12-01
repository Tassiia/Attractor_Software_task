from django.urls import reverse_lazy
from django.views.generic import DeleteView

from accounts.models import CustomUser


class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'users/delete_user.html'
    success_url = reverse_lazy('accounts:users_list')
    context_object_name = 'person'
