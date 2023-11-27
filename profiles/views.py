from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from products.models import Product
from .forms import UserProfileForm
from django.contrib import messages
from payment.models import Order
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    favorites = Product.objects.filter(favorites=request.user)
    products = Product.objects.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.warning(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'favorites': favorites,
        'products': products,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Display the user's order history. """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'payment/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


@login_required
def favorites_add(request, id):
    """ Add a product to the user's favorites. """

    product = get_object_or_404(Product, id=id)
    if product.favorites.filter(id=request.user.id).exists():
        messages.warning(request, f'{product.name} removed from favorites!')
        product.favorites.remove(request.user)
    else:
        messages.success(request, f'{product.name} added to favorites!')
        product.favorites.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
