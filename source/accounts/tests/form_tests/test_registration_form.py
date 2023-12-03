from django.test import TestCase

from accounts.forms import RegistrationForm


class TestRegistrationForm(TestCase):
    def setUp(self) -> None:
        self.correct_data = {
            'username': 'test_user',
            'password1': 'Aaaaaaaa1',
            'password2': 'Aaaaaaaa1',
        }

    def test_register_form_valid(self):
        form = RegistrationForm(self.correct_data)
        self.assertTrue(form.is_valid())

    def test_register_form_username_empty(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['username'] = ''
        form = RegistrationForm(incorrect_data)
        self.assertFalse(form.is_valid())

    def test_register_form_different_passwords(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['password2'] = '123'
        form = RegistrationForm(incorrect_data)
        self.assertFalse(form.is_valid())