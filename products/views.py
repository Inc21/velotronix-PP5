from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models.functions import Lower
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    visible = products.filter(hidden=False)

    query = ""
    categories = ""
    sort = ""
    direction = ""
    current_sorting = ""
    brands = ""
    on_sale = False

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if 'direction' in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{ sortkey }"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "on_sale" in request.GET:
            # get_sale = request.GET["on_sale"].split(",")
            products = products.filter(on_sale=True)
            on_sale = products
            # on_sale = Product.objects.filter(on_sale=True)
            print(on_sale)

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

            queries = Q(
                name__icontains=query) | Q(specs__icontains=query)
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
        'on_sale': on_sale,
        'visible': visible,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    favorites = Product.objects.filter(favorites=request.user.id)
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'favorites': favorites,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def product_admin(request):
    """
    A view all products within product admin page"""
    products = Product.objects.all()
    visible = products.filter(hidden=False)
    hidden = products.filter(hidden=True)

    template = "products/product_admin.html"
    context = {
        'products': products,
        'visible': visible,
        'hidden': hidden,
    }
    return render(request, template, context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully added a product!")
            return redirect(reverse("add_product"))
        else:
            messages.warning(
                request, "Failed to add product. \
                    Please ensure the form is valid.")
    else:
        form = ProductForm()
    template = "products/add_product.html"
    context = {
        "form": form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.warning(
                request,
                f'Failed to update {product.name}. Please\
                    ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete/hide a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.hidden = True
    product.save()
    messages.success(request, f'{product.name} deleted!')
    return redirect(reverse('product_admin'))


@login_required
def unhide_product(request, product_id):
    """ unhide a product from """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.hidden = False
    product.save()
    messages.success(request, f'{product.name} reactivated!')
    return redirect(reverse('product_admin'))
