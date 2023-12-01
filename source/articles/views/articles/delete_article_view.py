from django.views.generic import DeleteView

from articles.models import Article


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'articles/delete_article.html'
    success_url = '/'
    context_object_name = 'article'
