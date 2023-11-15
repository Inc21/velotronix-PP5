from django.shortcuts import render, redirect
from django.contrib import messages


def cart(request):
    """ A view to return the shopping cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    item_in_cart = item_id in list(cart.keys())
    item_quantity = cart

    if item_in_cart and cart[item_id] >= 90 or quantity > 90:
        print(item_quantity)
        messages.warning(request, 'You can only add 99 items per product!')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity
        if quantity == 1:
            print(cart[item_id])
            messages.success(request, f'{ quantity } item added to your cart!')
            print(quantity)
        else:
            messages.success(request, f"{ quantity } item's added to your cart!")

    request.session['cart'] = cart
    return redirect(redirect_url)
