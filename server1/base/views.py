from django.shortcuts import render
import requests

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html', {})


def products_api(request):
    url = 'http://127.0.0.1:8001/api/products/'
    products = {}
    
    try:
        r = requests.get(url)
        products = r.json()
    except Exception as e:
        print('Error: ',  e)
        products['products'] = []

    context = {
        "products": products['products']
    }
    return render(request, 'products/products.html', context)


def product_api(request, product_code):
    context = {
        'product_code': product_code
    }
    return render(request, 'products/product.html', context)
    pass