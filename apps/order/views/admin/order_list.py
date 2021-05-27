from django.views import View
from django.shortcuts import render, reverse
from django.http import JsonResponse
from django_datatables_too.mixins import DataTableMixin
from order.models import Order
from django.db.models import Q
from django_boilerplate.views.generic import MyListView

class OrderListView(MyListView):
    
    template_name = 'admin/order_list.html'
    model = Order
    queryset = model.objects.all()
    ordering = ["id"]
    permission_required = ("view_product",)
    
    
class DataTablesAjaxPagination(DataTableMixin, View):
    
    model = Order
    queryset = Order.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        details_view = reverse("order-details", kwargs={'pk':obj.pk})
        return f"""
                    <a href="{details_view}" title="Edit" class="btn btn-primary btn-xs">
                        <i class="fa fa-eye"></i>
                    </a>
                """

    def is_orderable(self):
        """Check if order is defined in dictionary."""
        return True

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            if self.search.isdecimal():   
                return qs.filter(
                    Q(order_id__icontains=self.search) 
                )
            return qs.filter(
                Q(transaction_id__icontains=self.search) |
                Q(user__email__icontains=self.search) 
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables

        data = []
        for o in qs:
            image = ''
                                  
            data.append({
                'id': o.id,
                'order_id': o.order_id,
                "total_amount": o.total_amount,
                'transaction_id': o.transaction_id,
                'user': o.user.email,
                'status':o.status,
                'card': o.card.last4 if o.card else '',
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