from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('products/', views.products_api, name='products'),
    path('products/<str:product_code>', views.product_api, name='product'),
]