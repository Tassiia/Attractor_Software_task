from rest_framework import serializers

from articles.models import Category


class CategoryTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']
