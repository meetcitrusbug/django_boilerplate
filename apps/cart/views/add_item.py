from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from cart.models import Cart
from product.models import Product


class AddItemView(View):
    
    def get(self, request, pk):
               
        next_url = self.get_next_url(request)
                
        if request.user.is_authenticated:
            self.add_items_in_database(pk)
        else:
            if request.session.get('cart'):
                request.session['cart'] = self.add_items_in_session(request.session['cart'], pk)
            else:
                request.session['cart'] = self.add_items_in_session([], pk)
                
        return redirect(next_url)

    def add_items_in_session(self, cart, id):
        """
        Add item(s) to session and update item(s) count 
        """
        item_exits = False
        for cart_item in cart:
            if id == cart_item['product']:
                cart_item['quantity'] += 1
                item_exits = True
        if not item_exits:
            new_item = {'product':id,'quantity':1} 
            cart = [*cart, new_item]
        return cart
    
    def add_items_in_database(self, pk):
        """
        Add item(s) to database and update item(s) count 
        """
        cart = Cart.objects.filter(product_id=pk, user=self.request.user).first()
       
        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                product=Product.objects.get(id=pk),
                user=self.request.user,
                quantity=1
            )
    
    def get_next_url(self, request):
        """
        Prepare url to redirect next after add item(s) to cart
        """
        next_url = ''
        for key in request.GET:
            if key =='next':
                next_url = request.GET[key]
            else:
                next_url += '&{}={}'.format(key, request.GET[key])
        return next_url