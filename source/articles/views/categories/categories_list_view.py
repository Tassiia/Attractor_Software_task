from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from articles.models import Category


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'categories/categories_list.html'
    context_object_name = 'categories'
