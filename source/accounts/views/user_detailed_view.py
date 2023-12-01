from django.views.generic import DetailView

from accounts.models import CustomUser


class UserDetailedView(DetailView):
    model = CustomUser
    template_name = 'users/user_detailed.html'
    context_object_name = 'person'
