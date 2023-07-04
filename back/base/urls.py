from django.urls import path
from .views import products_view

urlpatterns = [
    path('products/', products_view.as_view()),
    path('products/category/<str:category>/', products_view.as_view(), name='products_by_category'),
]
