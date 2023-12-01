from django import forms

from articles.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent']
