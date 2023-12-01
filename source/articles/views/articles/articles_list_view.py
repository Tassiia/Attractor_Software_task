from django.views.generic import ListView

from articles.models import Category, Article


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles'
