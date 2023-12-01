from django.urls import path

from articles.views.categories import AddCategoryView, CategoriesList, UpdateCategory

app_name = 'articles'

urlpatterns = [
    path('categories/', CategoriesList.as_view(), name='categories_list'),
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    path('categories/<int:pk>/change/', UpdateCategory.as_view(), name='update_category'),
]
