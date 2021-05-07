from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from cart.models import Cart
from product.models import Product

class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        if request.user.is_authenticated:
            return redirect('products')
        return render(request=request, template_name="django_template/userlogin.html", context={"login_form":form})

    def post(self, request):
        self.request = request
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                self.retrive_items_from_local_storage()
                return redirect('products')
            else:
                return redirect('login')
        else:
            return redirect('login')
        
    def retrive_items_from_local_storage(self):
        cart = self.request.session.get('cart')

        if cart:
            cart = cart.copy()
            for item in cart:
                product = self.get_product(item['product'])
                if product:
                    cart = Cart.objects.select_related('product').filter(
                                        product=product, user=self.request.user).first()
                    if cart:
                        cart.quantity += item['quantity']
                        cart.save()
                    else:
                        item['product'] = product
                        item['user'] = self.request.user
                        Cart.objects.create(**item)
                        
            self.request.session['cart'] = None                        
    
    def get_product(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None


def userlogout(request):
    logout(request)
    return redirect('login')