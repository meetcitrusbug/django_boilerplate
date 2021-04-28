from django.views import View
from django.shortcuts import render, reverse
from category.models import Category
from django_datatables_too.mixins import DataTableMixin
from django.http import JsonResponse
from django.db.models import Q
from django_boilerplate.views.generic import (
    MyListView,
)


class CategoryListView(MyListView):
    
    template_name = 'category_list.html'
    model = Category
    queryset = model.objects.all()
    ordering = ["id"]
    permission_required = ("view_category",)
    
    # def get(self, request, *args, **kwargs):
        
    #     return render(request, self.template, context=self.get_context())
    
    
class CategoryDataTablesAjaxPagination(DataTableMixin, View):
    
    model = Category
    queryset = Category.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("category-update", kwargs={'pk':obj.pk})
        delete_url = reverse("category-delete", kwargs={'pk':obj.pk})
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
                Q(name__icontains=self.search) 
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables

        data = []
        for o in qs:
            
            data.append({
                'id': o.id,
                'name': o.name,
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