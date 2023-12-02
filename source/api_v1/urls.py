from django.urls import path

from api_v1.views import ArticlesList, CategoriesList

urlpatterns = [
    path('articles/', ArticlesList.as_view(), name='articles_list_api_v1'),
    path('categories/', CategoriesList.as_view(), name='categories_list_api_v1'),
]
