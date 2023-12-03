from http import HTTPStatus

from django.urls import reverse_lazy, reverse

from accounts.tests.utils import CustomTestCase, login_as_admin
from articles.models import Category


class TestUpdateCategoryView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.old_category = Category.objects.create(
            title='old_category_title',
            parent=None,
        )
        self.old_category.save()
        self.correct_data = {
            'title': 'new_category_title',
            'parent': '',
        }
        self.url = reverse_lazy('articles:update_category', kwargs={'pk': self.old_category.pk})

    @login_as_admin
    def test_update_category_successfully(self):
        response = self.client.post(path=self.url, data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse_lazy('articles:categories_list'))
        self.assertEqual(Category.objects.first().title, 'new_category_title')

    def test_update_category_no_permission(self):
        response = self.client.post(path=self.url, data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+self.url)
        self.assertEqual(Category.objects.first().title, 'old_category_title')

    @login_as_admin
    def test_update_category_empty_title(self):
        incorrect_data = {
            'title': '',
            'parent': ''
        }
        response = self.client.post(self.url, data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Category.objects.first().title, 'old_category_title')

    @login_as_admin
    def test_update_category_invalid_parent(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['parent'] = self.old_category
        response = self.client.post(self.url, data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(self.old_category.parent, None)
