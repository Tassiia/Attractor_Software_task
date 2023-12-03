from http import HTTPStatus

from django.urls import reverse

from accounts.tests.utils import login_as_admin, CustomTestCase
from articles.models import Category


class TestAddCategoryView(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.correct_data = {
            'title': 'title_test',
            'parent': '',
        }

    @login_as_admin
    def test_add_category_valid(self):
        response = self.client.post(reverse('articles:add_category'), data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('articles:categories_list'))
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().title, 'title_test')

    def test_add_category_no_permission(self):
        response = self.client.post(reverse('articles:add_category'), data=self.correct_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('accounts:login')+'?next='+reverse('articles:add_category'))
        self.assertEqual(Category.objects.count(), 0)

    @login_as_admin
    def test_add_category_empty_title(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['title'] = ''
        response = self.client.post(reverse('articles:add_category'), data=incorrect_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Category.objects.count(), 0)

    @login_as_admin
    def test_add_category_incorrect_parent(self):
        parent_category = Category.objects.create(title='parent_category', parent=None)
        child_category_data = {
            'title': 'child_category',
            'parent': parent_category,
        }
        response = self.client.post(reverse('articles:add_category'), data=child_category_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().title, 'parent_category')
