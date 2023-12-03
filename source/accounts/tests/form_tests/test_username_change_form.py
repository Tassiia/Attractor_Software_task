from django.test import TestCase

from accounts.forms import UsernameChangeForm


class TestUsernameChangeForm(TestCase):
    def test_username_change_form_valid(self):
        correct_data = {'username': 'test_username'}
        form = UsernameChangeForm(correct_data)
        self.assertTrue(form.is_valid())

    def test_username_change_form_empty(self):
        correct_data = {'username': ''}
        form = UsernameChangeForm(correct_data)
        self.assertFalse(form.is_valid())
