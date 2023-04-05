from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
from django.core import serializers
from django.forms.models import model_to_dict
import json
from api.models import (
    Products
)
from api.forms import ProductsForm, ProductsUpdateForm
# Create your views here.

def index(request):
    """pagina inicial para api"""
    return JsonResponse({"status": 'success', "message": "welcome to the api"}, safe=False)


def get_all(request):
    # POST create Product
    if request.method == "POST":
        form = ProductsForm(request.POST or None)
        if form.is_valid():
            result = form.save()
            product = model_to_dict(result)
            return JsonResponse({"status": 'success', "message": "Create successfully", "product":product}, safe=False)
        else:
            return JsonResponse({"status": "error", "message": "Invalid Data"}, safe=False)
    
    products = list(Products.objects.all().values())
    return JsonResponse({"status": 'success', "products":products}, safe=False)


def get_one(request, product_code):
    product = Products.objects.filter(code=product_code)
    if not product:
            return JsonResponse({"status": "error", "message": "The product with that code does not exist"}, safe=False)
    
    # DELETE
    if request.method == "DELETE":
        result = product.delete()
        if result:
            return JsonResponse({"status": "success", "message": "Product successfully removed"}, safe=False)
        else:
            return JsonResponse({"status": "error", "message": "Error deleting the product"}, safe=False)
    
    # UPDATE
    if request.method == "POST":
        form = ProductsUpdateForm(request.POST or None)
        if form.is_valid():
            update = product.update(buy=request.POST.get("buy"), sell=request.POST.get("sell"))
            if update:
                new_product = Products.objects.filter(code=product_code)
                update_product = model_to_dict(new_product.first())
                return JsonResponse({"status": 'success', "message": "Product update successfully", "product":update_product}, safe=False)
            else:
                return JsonResponse({"status": "error", "message": "Error updating product"}, safe=False)
        else:
            return JsonResponse({"status": "error", "message": "Invalid Data"}, safe=False)
    
    # GET
    response = model_to_dict(product.first())
    return JsonResponse(response, safe=False)
