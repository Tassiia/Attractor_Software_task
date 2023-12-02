from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from articles.forms import CategoryUpdateForm
from articles.models import Category


class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryUpdateForm
    template_name = 'categories/update_category.html'
    success_url = '/'
