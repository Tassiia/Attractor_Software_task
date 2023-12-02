from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegistrationForm
from accounts.models import CustomUser


class AddUserView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('accounts:users_list')
