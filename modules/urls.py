# product_management/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('search/', views.search_product, name='search_product'),
    # Add other URL patterns as needed
]
