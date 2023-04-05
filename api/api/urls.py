from django.urls import path
from api import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', csrf_exempt(views.index), name='index'),
    path('products/', csrf_exempt(views.get_all), name='get_all'),
    path('products/<str:product_code>', csrf_exempt(views.get_one), name='get_one'),
]