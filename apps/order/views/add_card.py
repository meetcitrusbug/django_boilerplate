from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages

from order.models import  UserCard
from order.forms import CardAddForm

class AddCardView(View):
    
    template_name = "add_card.html"
    model = UserCard
    form = CardAddForm
    kwargs = {}
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, self.get_context_data())
        return redirect('login')
    
    def get_context_data(self):
        self.kwargs['form'] = self.form
        return  self.kwargs
        
        
    def post(self, request):
        form = self.form(data=request.POST, request=request)
        
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Card added")
                return redirect('cards')    
            except Exception as e:
                messages.error(request, str(e))

            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)
        else:
            context_data = self.get_context_data()
            context_data['form'] = form
            return render(request, self.template_name, context_data)
        