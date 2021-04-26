from notification.models import GroupUser
from customadmin.forms import CreateGroupUserForm
from django.shortcuts import reverse, render
from django.views import View
from django.http import JsonResponse
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q


class GroupUserListView(View):
    template = 'customadmin/groupuser/list_groupuser.html'
    model = GroupUser
    context = {
        'model_name':model._meta.model_name
    }
    
    def get(self, request):
        return render(request, self.template, context=self.updateContext())

    def updateContext(self):
        return self.context
     

class AddGroupUserView(CreateView):
    model = GroupUser
    form_class = CreateGroupUserForm
    template_name = 'customadmin/groupuser/add_groupuser.html'
    permission_required = ("core.add_groupuser",)
    
    def get_context_data(self):
        context = super(AddGroupUserView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("groupuser-list")


class EditGroupUserView(UpdateView):
    model = GroupUser
    form_class = CreateGroupUserForm
    template_name = 'customadmin/groupuser/edit_groupuser.html'
    permission_required = ("core.edit_groupuser",)
    
    def get_context_data(self):
        context = super(EditGroupUserView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_message(self):
        """Get success message"""
        print("-=-=-=-=-=-=-=-=-=priting message=-=-=-=-=-=-=-=-=-")
        return "{0} save successfully".format(self.model._meta.model_name)
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("groupuser-list")


class DeleteGroupUserView(DeleteView):
    model = GroupUser
    form_class = CreateGroupUserForm
    template_name = 'customadmin/groupuser/delete_groupuser.html'
    permission_required = ("core.delete_groupuser",)
    
    def get_context_data(self, object):
        context = super(DeleteGroupUserView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("groupuser-list")


class GroupUserDataTablesAjaxPagination(DataTableMixin, View):
    model = GroupUser
    queryset = GroupUser.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("edit-groupuser", kwargs={'pk':obj.pk})
        delete_url = reverse("delete-groupuser", kwargs={'pk':obj.pk})
        return f"""
                    <a href="{edit_url}" title="Edit" class="btn btn-primary btn-xs">
                        <i class="fa fa-pencil"></i>
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
                Q(group_name__group_name__icontains=self.search) |
                Q(user__username__icontains=self.search) 
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append({
                'group_name': o.group_name.group_name,
                'user': o.user.username,
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