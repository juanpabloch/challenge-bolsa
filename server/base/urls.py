from django.urls import path, include
from base import views

urlpatterns = [
    path('', views.products_api, name='products'),
    path('<str:product_code>', views.product_api, name='product'),
]