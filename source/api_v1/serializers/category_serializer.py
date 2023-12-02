from rest_framework import serializers

from api_v1.serializers.category_title_serializer import CategoryTitleSerializer
from articles.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = CategoryTitleSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['title', 'parent']
