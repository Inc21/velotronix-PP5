from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = ""

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.info(request, "You didn't enter any search criteria!")
                query = ""
                return redirect(reverse("products"))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            if products.filter(queries).count() == 0:
                messages.info(
                    request, f'The term "{ query }" was not found in products \
                        or descriptions!')
                return redirect(reverse("products"))
            else:
                query = request.GET["q"]
                products = products.filter(queries)
                messages.success(
                    request, f' You searched for "{ query }"')

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
