from django import forms

from articles.models import Category, Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category', 'user', 'title', 'description', 'image']
