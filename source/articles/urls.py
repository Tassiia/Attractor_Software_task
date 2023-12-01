from django.urls import path

from articles.views.categories import AddCategoryView, CategoriesList

app_name = 'articles'

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name='categories_list'),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
]
