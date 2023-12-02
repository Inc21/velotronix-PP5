from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def cart(request):
    """ A view to return the shopping cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart"""
    quantity = request.POST.get('quantity')
    redirect_url = request.POST.get('redirect_url')
    if quantity is None or quantity == '0' or quantity == '':
        messages.warning(request, 'Please select a quantity!')
        return redirect(reverse('products'))
    else:
        quantity = int(quantity)
    print(quantity)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity > 99:
        cart[item_id] = 99
        messages.warning(request, 'You can only add 99 items per product!')
    else:
        if item_id in list(cart.keys()) and cart[item_id] + quantity > 99:
            cart[item_id] = 99
            messages.warning(
                request, 'You can only add 99 items per product!')
        else:
            if item_id in list(cart.keys()):
                cart[item_id] += quantity
            else:
                cart[item_id] = quantity
            if quantity == 1:
                print(cart[item_id])
                messages.success(
                    request, f'{ quantity } item added to your cart!')
                print(quantity)
            else:
                messages.success(
                    request, f"{ quantity } item's added to your cart!")

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust the quantity of the specified
    product to the specified amount
    """
    if (request.POST.get('quantity') == '' or
            request.POST.get('quantity') is None):
        messages.warning(request, 'Please select a quantity!')
        return redirect(reverse('cart'))
    else:
        quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity is None or quantity == '0' or quantity == '':
        messages.warning(request, 'Please select a quantity!')
        return redirect(reverse('products'))
    else:
        quantity = int(quantity)

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(
            request, f'Updated item quantity to { quantity }')
    else:
        cart.pop(item_id)
        messages.info(request, 'Item removed from your cart!')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """ Remove the item from the shopping cart """
    cart = request.session.get('cart', {})

    try:
        cart.pop(item_id)
        messages.info(request, 'Item removed from your cart!')

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.warning(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
