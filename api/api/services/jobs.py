from api.models import Products
from django.db.models import F, DecimalField, ExpressionWrapper

def update_products():
    products = Products.objects.all()
    products = products.annotate(new_buy=ExpressionWrapper(F('buy')*1.05, output_field=DecimalField()))
    products = products.annotate(new_sell=ExpressionWrapper(F('sell')*1.05, output_field=DecimalField()))
    
    for obj in products:
        obj.sell = obj.new_sell
        obj.buy = obj.new_buy
        obj.save()
    
    print("UPDATE price complete")