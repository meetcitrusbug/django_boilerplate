from django.views import View
from cart.models import Cart
from django.shortcuts import redirect    

class RemoveAllCartItemView(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            Cart.objects.filter(user=request.user).delete()
        else:
            request.session['cart'] = None
        return redirect('cart-list')