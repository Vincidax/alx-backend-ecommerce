from django.urls import path
from .views import ListCategory, DetailCategory, ListBook, DetailBook, ListProduct, DetailProduct
urlpatterns = [
    path('categories', ListCategory.as_view(), name='categorie'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name= 'singlecategory'),
    path('book', ListBook.as_view(), name='books'),
    path('book/<int:pk>/', DetailBook.as_view(), name= 'singlebook'),
    path('product', ListProduct.as_view(), name='categorie'),
    path('product/<int:pk>/', DetailProduct.as_view(), name= 'singleproduct'),
]
