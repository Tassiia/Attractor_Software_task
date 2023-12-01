from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from accounts.models import CustomUser


class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']

    def clean_username(self):
        new_username = self.cleaned_data.get('username')
        if new_username == self.instance.username:
            raise ValidationError(_('New username should be different from the previous one'))
        elif new_username in CustomUser.objects.values('username'):
            raise ValidationError(_('This username is already taken'))
        return new_username
