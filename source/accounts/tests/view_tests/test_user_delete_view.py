from http import HTTPStatus

from django.urls import reverse_lazy, reverse

from accounts.models import CustomUser
from accounts.tests.utils import CustomTestCase, login_as_admin


class TestUserDeleteView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.url = reverse_lazy('accounts:delete_user', kwargs={'pk': self.user.pk})

    @login_as_admin
    def test_delete_user_successfully(self):
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertRedirects(response, reverse_lazy('accounts:users_list'))
        self.assertEqual(CustomUser.objects.first().username, 'admin')

    def test_delete_user_no_permission(self):
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+self.url)
