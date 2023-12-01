from django.urls import path

from articles.views.categories import AddCategoryView, CategoriesList, UpdateCategory, DeleteCategory
from articles.views.articles import ArticlesListView, AddArticleView, UpdateArticleView, DeleteArticleView

app_name = 'articles'

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name='categories_list'),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    path('categories/<int:pk>/change/', UpdateCategory.as_view(), name='update_category'),
    path('categories/<int:pk>/delete/', DeleteCategory.as_view(), name='delete_category'),

    path('articles/', ArticlesListView.as_view(), name='articles_list'),
    path('articles/add/', AddArticleView.as_view(), name='add_article'),
    path('articles/<int:pk>/change/', UpdateArticleView.as_view(), name='update_article'),
    path('articles/<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
]
