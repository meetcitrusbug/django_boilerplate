from django.views import View
from django.shortcuts import render, reverse
from category.models import SubCategory
from django_datatables_too.mixins import DataTableMixin
from django.http import JsonResponse
from django.db.models import Q
from django_boilerplate.views.generic import (
    MyListView,
)

class SubCategoryListView(MyListView):
    
    template_name = 'subcategory/subcategory_list.html'
    model = SubCategory
    queryset = model.objects.all()
    ordering = ["id"]
    permission_required = ("view_subcategory",)
    
    # def get(self, request, *args, **kwargs):
        
    #     return render(request, self.template, context=self.get_context())

    
    # def get_context(self):
    #     context = self.context
    #     context["model_name"] = self.model._meta.model_name
    #     return self.context
    
    
class SubCategoryDataTablesAjaxPagination(DataTableMixin, View):
    
    model = SubCategory
    queryset = SubCategory.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("subcategory-update", kwargs={'pk':obj.pk})
        delete_url = reverse("subcategory-delete", kwargs={'pk':obj.pk})
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