from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})
def cart(request):
    return render(request, 'store/cart.html')
def register(request):
    return render(request, 'store/register.html')
def login(request):
    return render(request, 'store/login.html')
def order_success(request):
    return render(request, 'store/order_success.html')