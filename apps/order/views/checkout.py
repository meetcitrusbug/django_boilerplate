from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.db.models import Sum
from django.db.models import F
from django.contrib import messages

from order.models import Order, UserCard
from cart.models import Cart
from order.forms import CheckoutForm, CheckoutCardForm

class CheckoutDetailsView(View):
    
    template_name = "checkout.html"
    model = Order
    form = CheckoutForm
    kwargs = {}
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, self.get_context_data())
        return redirect('login')
    
    def get_context_data(self):
        self.kwargs['obj'] = self.get_object(self.kwargs.get('pk'))
        self.kwargs['total_price'] = self.get_total_price(self.request.user)
        self.kwargs['cards'] = self.get_card_list(self.request.user)
        self.kwargs['form'] = self.form
        return  self.kwargs
    
    def get_card_list(self, user):
        return UserCard.objects.filter(user=user)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None
        
    def get_total_price(self, user):
        total_price = Cart.objects.filter(user=user).values('user').aggregate(
                                    total_price=Sum(F('product__price')* F("quantity")))
        return total_price.get('total_price',0)
    
    
    def post(self, request):
        form = self.form(data=request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Order place successfully")
                return redirect('checkout')    
            except Exception as e:
                messages.error(request, str(e))

            context_data = self.get_context_data()
            context_data['form'] = form
            return redirect('checkout') 
        else:
            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)
        

class CheckoutWithCardView(View):
    
    
    template_name = "checkout.html"
    model = Order
    form = CheckoutCardForm
    kwargs = {}
       
    def get_context_data(self):
        self.kwargs['obj'] = self.get_object(self.kwargs.get('pk'))
        self.kwargs['total_price'] = self.get_total_price(self.request.user)
        self.kwargs['cards'] = self.get_card_list(self.request.user)
        self.kwargs['form'] = self.form
        return  self.kwargs
    
    def get_card_list(self, user):
        return UserCard.objects.filter(user=user)

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return None
        
    def get_total_price(self, user):
        total_price = Cart.objects.filter(user=user).values('user').aggregate(
                                    total_price=Sum(F('product__price')* F("quantity")))
        return total_price.get('total_price',0)
    
    
    def post(self, request):
        form = self.form(data=request.POST)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Order place successfully")
                return redirect('checkout')    
            except Exception as e:
                print('============',e)
                messages.error(request, str(e))

            context_data = self.get_context_data()
            context_data['form'] = form
            return redirect('checkout')
        else:
            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)