from django.views import View
from django.shortcuts import render
from django_boilerplate.utils.cart_item_counter import get_cart_item_count
from product.models import Product
from cart.models import Cart

class CartListAPIView(View):
    
    template_name = 'cart_list.html'
    request = None
        
    def get(self, request, *args, **kwargs):
        self.request = request
        return render(request, self.template_name, context=self.get_context_data())
    
    
    def get_context_data(self):
        ctx = {}
        ctx['cart_count'] =  get_cart_item_count(self.request)
        ctx['query'] = self.get_queryset()
        return ctx
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Cart.objects.filter(user=self.request.user)
        else:
            if self.request.session.get('cart'):
                cart = self.request.session.get('cart').copy()
            else:
                cart = []
            for i in cart:
                i['product'] = self.get_product(i['product'])
            return cart
        
    def get_product(self, id):
        try:
            return Product.objects.get(id= id)
        except Product.DoesNotExist:
            return None