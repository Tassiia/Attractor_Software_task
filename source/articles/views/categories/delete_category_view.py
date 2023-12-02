from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from articles.models import Category


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    success_url = reverse_lazy('articles:categories_list')
    context_object_name = 'category'
