from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from articles.models import Category, Article


class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles'
