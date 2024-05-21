from django.shortcuts import render
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    all_quantity = Order.objects.aggregate(Sum('quantity_ordered'))
    total_total = Order.objects.aggregate(Sum('total_price'))
    print(all_quantity)
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    context = {
        'price' : price_from_form, 'quantity': quantity_from_form, 'total': total_charge, 'all_q' : str(all_quantity['quantity_ordered__sum']), 'total_total': str(total_total['total_price__sum']), 
    }
    return render(request, "store/checkout.html", context)