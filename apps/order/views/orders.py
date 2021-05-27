from django.views import View
from django.shortcuts import render, redirect
from order.models import Order
from django.db.models import Q
from django.contrib import messages

class OrdersList(View):
    
    template_name = 'orders.html'
    model = Order
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

        if search and search.isdecimal():
            return query.filter(
                Q(order_id=search)  | Q(total_amount=search)
            )
            
        if search:
            query = query.filter(
                Q(transaction_id=search) | Q(status=search)
            )
        return query