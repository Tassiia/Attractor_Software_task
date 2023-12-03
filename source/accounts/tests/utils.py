from django.test import TestCase

from accounts.models import CustomUser


class CustomTestCase(TestCase):
    def setUp(self) -> None:
        self.admin = CustomUser.objects.create(username='admin')
        self.admin.set_password('Aaaaaaaa1')
        self.admin.save()

        self.user = CustomUser.objects.create(username='user')
        self.user.set_password('Aaaaaaaa1')
        self.user.save()


def login_as_admin(func):
    def wrapper(self, *args, **kwargs):
        self.client.login(username='admin', password='Aaaaaaaa1')
        func(self, *args, **kwargs)
    return wrapper
