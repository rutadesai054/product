from django.shortcuts import render, get_object_or_404
from .models import Product_mst, Product_sub_cat

def product_details(request, product_id):
    product = get_object_or_404(Product_mst, pk=product_id)
    subcategory_details = Product_sub_cat.objects.filter(product=product)
    return render(request, 'product_details.html', {'product': product, 'subcategory_details': subcategory_details})

def search_product(request):
    query = request.GET.get('q')
    if query:
        products = Product_mst.objects.filter(product_name__icontains=query)
    else:
        products = Product_mst.objects.all()
    return render(request, 'search_product.html', {'products': products})
