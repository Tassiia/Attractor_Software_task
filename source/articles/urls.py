from django.urls import path

from articles.views.categories import AddCategoryView

app_name = 'articles'

urlpatterns = [
    path('categories/add/', AddCategoryView.as_view(), name='add_category'),
]
