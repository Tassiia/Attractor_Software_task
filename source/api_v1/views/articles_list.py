from rest_framework.generics import ListAPIView

from api_v1.serializers.article_serializer import ArticleSerializer
from articles.models import Article


class ArticlesList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
