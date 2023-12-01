from django.views.generic import CreateView

from accounts.forms import RegistrationForm
from accounts.models import CustomUser


class RegistrationView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'users/registration.html'
    success_url = '/'
