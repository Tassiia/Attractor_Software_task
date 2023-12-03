from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import UsernameChangeForm
from accounts.models import CustomUser


class UsernameChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UsernameChangeForm
    template_name = 'users/change_username.html'

    def get_success_url(self):
        user_pk = self.object.pk
        return reverse_lazy('accounts:users_list')
