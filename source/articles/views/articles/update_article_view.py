from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from articles.forms import ArticleForm
from articles.models import Article


class UpdateArticleView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/update_article.html'
    success_url = '/'
