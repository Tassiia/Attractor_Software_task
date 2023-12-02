from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from accounts.forms import UsernameChangeForm
from accounts.models import CustomUser


class UsernameChangeView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UsernameChangeForm
    template_name = 'users/change_username.html'
    success_url = '/'
