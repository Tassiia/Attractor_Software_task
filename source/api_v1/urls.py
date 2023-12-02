from django.urls import path

from api_v1.views.articles_list import ArticlesList

urlpatterns = [
    path('articles/', ArticlesList.as_view(), name='articles_list_api_v1'),
]
