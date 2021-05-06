# from django.views import View
from django.shortcuts import render, reverse
from product.models import Product, ProductImage, ProductTag
from category.models import Category
from django.db.models import Q
from django.views.generic import ListView
from django_boilerplate.utils.cart_item_counter import get_cart_item_count


class ProductView(ListView):
    
    template_name = 'product.html'
    paginate_by = 4
    model = Product
    context = {
        'model_name':model._meta.model_name
    }
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        context.update(self.update_context()) 
        return context
    
    def get_queryset(self):
        context = self.update_context()
               
        query = self.model.objects.filter(is_active=True)
        
        products =  ProductTag.objects.filter(tag__icontains=context['search']).values_list('product__id', flat=True)
               
        if context['search']:
            query = query.filter(Q(name__icontains=context['search']) 
                                 | Q(id__in=products) |
                                    Q(sub_category__category__name__icontains=context['search']) |
                                    Q(sub_category__name__icontains=context['search'])) 
        if context['selected_category']:
            query = query.filter(sub_category__category__in=context['selected_category'])
        if context['min']:
            query = query.filter(price__gte=context['min']) 
        if context['max']:
            query = query.filter(price__lte=context['max'])
            
        return query.order_by('-id')
    
    
    
    def update_context(self):
        search = self.request.GET.get('search','')
        page = self.request.GET.get('search','')
        min_ = self.request.GET.get('min','')
        max_ = self.request.GET.get('max','')
        page = self.request.GET.get('page','')
        cart_count =  get_cart_item_count(self.request) 
        
        selected_category = self.list_string_to_integer(
                                self.request.GET.getlist('selected_category',''))
        
        category = Category.objects.all()
                        
        context =  {
            "search":search,
            "page":page,
            "min":min_,
            "max":max_,
            "page":page,
            "category":category,
            "selected_category":selected_category,
            "cart_count":cart_count
        }
        return context
    
    def list_string_to_integer(self, list_):
        for i in range(0, len(list_)):
            list_[i] = int(list_[i])
            
        return list_