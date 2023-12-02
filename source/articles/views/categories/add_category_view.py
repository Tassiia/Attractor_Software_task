from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from articles.forms import CategoryForm
from articles.models import Category


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/add_category.html'
    success_url = reverse_lazy('articles:categories_list')
