from django.views.generic import DeleteView

from articles.models import Category


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'categories/delete_category.html'
    success_url = '/'
    context_object_name = 'category'
