from http import HTTPStatus

from django.urls import reverse_lazy, reverse

from accounts.models import CustomUser
from accounts.tests.utils import CustomTestCase, login_as_admin


class TestUsernameChangeView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.correct_data = {
            'username': 'new_username',
        }
        self.url = reverse_lazy('accounts:change_username', kwargs={'pk': self.user.pk})

    @login_as_admin
    def test_change_username_successfully(self):
        response = self.client.post(path=self.url, data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('accounts:users_list'))
        self.assertEqual(CustomUser.objects.get(pk=self.user.pk).username, 'new_username')

    def test_change_username_no_permission(self):
        response = self.client.post(path=self.url, data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+self.url)
        self.assertEqual(CustomUser.objects.get(pk=self.user.pk).username, 'user')

    @login_as_admin
    def test_change_username_empty_username(self):
        incorrect_data = {'username': ''}
        response = self.client.post(reverse('accounts:register_user'), data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(CustomUser.objects.get(pk=self.user.pk).username, 'user')
