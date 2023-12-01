from django.views.generic import CreateView

from articles.forms import CategoryForm
from articles.models import Category


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/add_category.html'
    success_url = '/'
