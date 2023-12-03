from django.test import TestCase

from articles.forms import CategoryForm


class TestCategoryForm(TestCase):
    def setUp(self) -> None:
        self.correct_data = {
            'title': 'new_title',
            'parent': None,
        }

    def test_category_form_valid(self):
        form = CategoryForm(self.correct_data)
        self.assertTrue(form.is_valid())

    def test_category_form_title_empty(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['title'] = ''
        form = CategoryForm(incorrect_data)
        self.assertFalse(form.is_valid())

    def test_category_invalid_parent(self):
        incorrect_data = self.correct_data.copy()
        incorrect_data['parent'] = '99'
        form = CategoryForm(incorrect_data)
        self.assertFalse(form.is_valid())
