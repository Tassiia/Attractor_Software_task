from rest_framework.generics import ListAPIView

from api_v1.serializers.category_serializer import CategorySerializer
from articles.models import Category


class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
