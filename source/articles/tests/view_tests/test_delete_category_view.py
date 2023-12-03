from http import HTTPStatus

from django.urls import reverse_lazy, reverse

from accounts.tests.utils import CustomTestCase, login_as_admin
from articles.models import Category


class TestDeleteCategoryView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.category = Category.objects.create(title='category_title', parent=None)
        self.url = reverse_lazy('articles:delete_category', kwargs={'pk': self.category.pk})

    @login_as_admin
    def test_delete_category_successfully(self):
        self.assertEqual(Category.objects.count(), 1)
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(Category.objects.count(), 0)
        self.assertRedirects(response, reverse_lazy('articles:categories_list'))

    def test_delete_category_no_permission(self):
        self.assertEqual(Category.objects.count(), 1)
        response = self.client.post(path=self.url)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+self.url)
        self.assertEqual(Category.objects.count(), 1)
