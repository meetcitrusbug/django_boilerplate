from django.views import View
from django.shortcuts import render, redirect
from order.models import UserCard
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
import stripe

class CardsList(View):
    
    template_name = 'cards.html'
    model = UserCard
    ordering = ["id"]

    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.request = request
        if request.user.is_authenticated:
            return render(request, self.template_name, self.get_context_data())
        return redirect('login')
    

    def get_context_data(self):
        self.kwargs['list'] = self.get_queryset()
        self.kwargs['search'] = self.request.GET.get('search')
        return  self.kwargs
    
    def get_queryset(self):
        search = self.request.GET.get('search')
        query = self.model.objects.filter(user=self.request.user).order_by('-id')

        if search :
            return query.filter(
                Q(card_number=search)
            )
        return query
    

class CardDeletView(View):
    
    model = UserCard
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        if instance:
            try:
                stripe.Customer.delete_source(
                        instance.user.customer_id,
                        instance.card_number,
                        )
                self.perform_destroy(instance)
                messages.success(request, 'Card deleted')
                return redirect('cards') 
            except Exception as e:
                messages.success(request, 'Can not delete card')
                return redirect('cards') 
        messages.success(request, 'Card not found')
        return redirect('cards') 
            
    def get_object(self, pk):
        return self.model.objects.filter(pk=pk).first()
    
    def perform_destroy(self, instance):
        instance.delete()