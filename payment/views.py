from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """ A view to return the checkout page """
    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'payment/checkout.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
