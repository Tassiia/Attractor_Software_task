from django.views.generic import CreateView

from articles.forms import ArticleForm
from articles.models import Article


class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/add_article.html'
    success_url = '/'
