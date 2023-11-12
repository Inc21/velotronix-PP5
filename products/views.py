from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = ""
    categories = ""
    sort = ""
    direction = ""
    current_sorting = ""
    brands = ""

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))

            if 'direction' in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{ sortkey }"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "brand" in request.GET:
            brands = request.GET["brand"].split(",")
            products = products.filter(brand__in=brands)

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

    current_sorting = f"{ sort }_{ direction }"

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'brands': brands,
        'sort': sort,
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
