from django.views import View
from django.shortcuts import render

from order.models import Order, OrderProduct


class OrderDetailsView(View):
    
    template_name = "order_details.html"
    model = Order
    kwargs ={}
    request = None
    
    def get(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.request = request
        return render(request,self.template_name, self.get_context_data())
    
    def get_object(self):
        try:
            return  self.model.objects.get(
                pk=self.kwargs.get('pk'))
        except:
            return None
        
    def get_context_data(self):
        return {
            'obj':self.get_object(),
            'items':OrderProduct.objects.filter(order=self.get_object())
        }