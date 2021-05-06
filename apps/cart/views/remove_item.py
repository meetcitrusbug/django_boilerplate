from django.views import View
from cart.models import Cart
from django.shortcuts import redirect
from django.contrib import messages

class CartItemRemoveView(View):
    
    def get(self, request, pk):
        self.request = request
        self.remove_items(pk)
        return redirect('cart-list')
                
    def remove_items(self, pk):
        if self.request.user.is_authenticated:
            cart = Cart.objects.select_related('product'
                    ).filter(product__pk=pk, user=self.request.user)
            cart.delete()
        else:
            cart = self.request.session.get('cart')
            item = None
            for i in cart:
                if pk == i['product']:
                    item = i    
            self.request.session['cart'] = [item for item in cart if not (pk == item.get('product'))]
                
                