from django.shortcuts import render, get_object_or_404
from .models import Product, Order

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})
def cart(request):
    product_id = request.GET.get('product_id')
    product = None

    if product_id:
        product = get_object_or_404(Product, id=product_id)

    return render(request, 'store/cart.html', {'product': product})
def register(request):
    return render(request, 'store/register.html')
def login(request):
    return render(request, 'store/login.html')
def order_success(request):
    product_id = request.GET.get('product_id')

    if product_id:
        product = get_object_or_404(Product, id=product_id)

        Order.objects.create(
            product=product,
            customer_name="Guest",
            quantity=1,
            total_price=product.price
        )

    return render(request, 'store/order_success.html')