from django.views import View
from django.shortcuts import render, reverse
from django.http import JsonResponse
from django_datatables_too.mixins import DataTableMixin
from product.models import Product, ProductImage, ProductTag
from django.db.models import Q
from django_boilerplate.views.generic import MyListView

class ProductListView(MyListView):
    
    template_name = 'product_list.html'
    model = Product
    queryset = model.objects.all()
    ordering = ["id"]
    permission_required = ("view_product",)
    
    
class DataTablesAjaxPagination(DataTableMixin, View):
    
    model = Product
    queryset = Product.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("product-update", kwargs={'pk':obj.pk})
        delete_url = reverse("product-delete", kwargs={'pk':obj.pk})
        return f"""
                    <a href="{edit_url}" title="Edit" class="btn btn-primary btn-xs">
                        <i class="fa fa-pencil-square"></i>
                    </a>
                    <a data-title="{delete_url}" title="Delete" href="{delete_url}" class="btn btn-danger btn-xs btn-delete">
                        <i class="fa fa-trash"></i>
                    </a>
                """

    def is_orderable(self):
        """Check if order is defined in dictionary."""
        return True

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(name__icontains=self.search) |
                Q(product_number__icontains=self.search) |
                Q(sub_category__name__icontains=self.search) |
                Q(product_shipping_method__icontains=self.search) |
                Q(status__icontains=self.search) |
                Q(price__icontains=self.search) 
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables

        data = []
        for o in qs:
            image = ''
            
            product_image = ProductImage.objects.select_related('product').filter(product=o).order_by('id').first()
            
            if product_image:
                image = '<image src="%s" height="50" widht="50"/>' % product_image.image.url
            
            data.append({
                'id': o.id,
                'name': o.name,
                "user": o.user.username if o.user else '',
                'product_number': o.product_number,
                'sub_category': o.sub_category.name,
                'status':o.status,
                'price':o.price,
                'product_shipping_method':o.product_shipping_method,
                'is_refundable': self.boolean_icon(o.is_refundable),
                'is_active': self.boolean_icon(o.is_active),
                'image':image,
                'actions':self._get_actions(o),
            })
        return data
    
    
    def boolean_icon(self, flag):
            if flag:
                return "<i style='color:green;' class='fa fa-check'></i>&nbsp; Yes"
            return "<i style='color:red;' class='fa fa-times'></i>&nbsp; No"

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)