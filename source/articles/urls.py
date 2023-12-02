from django.urls import path
from django.views.generic import RedirectView

from articles.views.categories import AddCategoryView, CategoriesListView, UpdateCategoryView, DeleteCategoryView
from articles.views.articles import ArticlesListView, AddArticleView, UpdateArticleView, DeleteArticleView

app_name = 'articles'

urlpatterns = [
    path('', RedirectView.as_view(permanent=True, url='articles/'), name='index'),

    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    path('categories/<int:pk>/change/', UpdateCategoryView.as_view(), name='update_category'),
    path('categories/<int:pk>/delete/', DeleteCategoryView.as_view(), name='delete_category'),

    path('articles/', ArticlesListView.as_view(), name='articles_list'),
    path('articles/add/', AddArticleView.as_view(), name='add_article'),
    path('articles/<int:pk>/change/', UpdateArticleView.as_view(), name='update_article'),
    path('articles/<int:pk>/delete/', DeleteArticleView.as_view(), name='delete_article'),
]
