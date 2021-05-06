from cart.models import Cart
from django.db.models import Sum

def get_cart_item_count(request):
    cart_count = None
    if request.user.is_authenticated:
        quantity = Cart.objects.filter(user=request.user)
        if quantity:
            quantity = quantity.aggregate(sum=Sum('quantity'))
            return quantity.get('sum', None)
        return None
    cart  = request.session.get('cart')
    if type(cart) == list:
        cart_count = 0
        for item in cart:
            cart_count += item['quantity']
    return cart_count