from http import HTTPStatus

from django.urls import reverse

from accounts.models import CustomUser
from accounts.tests.utils import login_as_admin, CustomTestCase


class TestAddUserView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.correct_data = {
            'username': 'created_user',
            'password1': 'Aaaaaaaa1',
            'password2': 'Aaaaaaaa1',
        }

    @login_as_admin
    def test_add_user_valid(self):
        response = self.client.post(reverse('accounts:register_user'), data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:users_list'))
        self.assertEqual(CustomUser.objects.count(), 3)
        self.assertEqual(CustomUser.objects.order_by('pk').last().username, 'created_user')

    def test_add_user_no_permission(self):
        response = self.client.post(reverse('accounts:register_user'), data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+reverse('accounts:register_user'))
        self.assertEqual(CustomUser.objects.count(), 2)

    @login_as_admin
    def test_add_user_empty_username(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['username'] = ''
        response = self.client.post(reverse('accounts:register_user'), data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(CustomUser.objects.count(), 2)

    @login_as_admin
    def test_add_user_not_matching_passwords(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['password2'] = '123'
        response = self.client.post(reverse('accounts:register_user'), data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(CustomUser.objects.count(), 2)
