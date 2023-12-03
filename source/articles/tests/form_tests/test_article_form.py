import base64

from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.tests.utils import CustomTestCase
from articles.forms import ArticleForm
from articles.models import Category


class TestArticleForm(CustomTestCase):
    def setUp(self) -> None:
        super().setUp()
        category = Category.objects.create(title='category_test', parent=None)
        category.save()

        self.correct_data = {
            'category': category,
            'user': self.user,
            'title': 'Title_test',
            'description': 'Description_test',
        }
        image_content = base64.b64decode("R0lGODlhAQABAIAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==")
        image = SimpleUploadedFile("image.jpg", image_content, content_type="image/jpeg")
        self.image_data = {'image': image}

    def test_article_form_valid(self):
        form = ArticleForm(self.correct_data, self.image_data)
        self.assertTrue(form.is_valid())

    def invalid_data(self, field, data):
        incorrect_data = self.correct_data.copy()
        incorrect_data[field] = data
        form = ArticleForm(incorrect_data, self.image_data)
        self.assertFalse(form.is_valid())

    def test_article_form_category_empty(self):
        self.invalid_data('category', None)

    def test_article_form_user_empty(self):
        self.invalid_data('user', None)

    def test_article_form_title_empty(self):
        self.invalid_data('title', '')

    def test_article_form_description_empty(self):
        self.invalid_data('description', '')

    def test_article_form_image_empty(self):
        form = ArticleForm(self.correct_data, {'image': None})
        self.assertFalse(form.is_valid())

    def test_article_form_invalid_category(self):
        self.invalid_data('category', 99)

    def test_article_form_invalid_image(self):
        form = ArticleForm(self.correct_data, {'image': 'not_an_image'})
        self.assertFalse(form.is_valid())
