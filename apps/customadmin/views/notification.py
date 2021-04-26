from notification.models import Notification, Group, GroupUser
from customadmin.forms import CreateNotificationForm
from django.shortcuts import reverse, render
from django.views import View
from django.http import JsonResponse
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django_datatables_too.mixins import DataTableMixin
from django.db.models import Q

from pyfcm import FCMNotification


class NotificationListView(View):
    template = 'customadmin/notification/list_notification.html'
    model = Notification
    context = {
        'model_name':model._meta.model_name
    }
    
    def get(self, request):
        return render(request, self.template, context=self.updateContext())

    def updateContext(self):
        return self.context
     

class AddNotificationView(CreateView):
    model = Notification
    form_class = CreateNotificationForm
    template_name = 'customadmin/notification/add_notification.html'
    permission_required = ("core.add_notification",)
    
    def get_context_data(self):
        context = super(AddNotificationView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("notification-list")


class EditNotificationView(UpdateView):
    model = Notification
    form_class = CreateNotificationForm
    template_name = 'customadmin/notification/edit_notification.html'
    permission_required = ("core.edit_notification",)
    
    def get_context_data(self):
        context = super(EditNotificationView, self).get_context_data()
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_message(self):
        """Get success message"""
        print("-=-=-=-=-=-=-=-=-=priting message=-=-=-=-=-=-=-=-=-")
        return "{0} save successfully".format(self.model._meta.model_name)
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("notification-list")


class DeleteNotificationView(DeleteView):
    model = Notification
    form_class = CreateNotificationForm
    template_name = 'customadmin/notification/delete_notification.html'
    permission_required = ("core.delete_notification",)
    
    def get_context_data(self, object):
        context = super(DeleteNotificationView, self).get_context_data(object=object)
        context['model_name'] = self.model._meta.model_name
        return context
    
    def get_success_url(self):
        """Get success URL"""
        return reverse("notification-list")

class NotificationSendView(View):
    def get(self, request, pk):
        notification = Notification.objects.get(pk=pk)
        message_title = notification.title
        message_body = notification.description
        api_key = "AAAA-F3kDws:APA91bENHxS72ai1So4PXQ1htHc2XhApysw_KksmyQWWy_aZe-Pq_-BrVP4yxY3dG452oPt3YLGzecjhLGL0ufs3rELk0Gidq9ZamPwl7caLyWKewE-3Vpv1EYKpBmmdv_EzrqxkLjeR"
        
        if notification.is_singleuser == False:
            group_name = Group.objects.get(pk=notification.group.pk)
            users = GroupUser.objects.filter(group_name=group_name)
            user_objects = []
            for i in users:
                user_objects.append(i.user)
            registration_ids = []
            for i in user_objects:
                registration_ids.append(i.username)
            push_service = FCMNotification(api_key=api_key)
            message_title = notification.title
            message_body = notification.description
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
            print(registration_ids, "----------------------")
            print(result, "============================")
        else:
            registration_id = notification.user.username
            push_service = FCMNotification(api_key=api_key)
            message_title = notification.title
            message_body = notification.description
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
            print(registration_id, "----------------------")
            print(result, "============================")

        flag = False
        if result['success'] == 1:
            flag = True
            message = "Notification sent successfully!"          
            print(message)
        else:
            message = "Notification isn't sent successfully!"
            print(message)
        
        return render(request,"customadmin/notification/result_notification.html", {'flag':flag})



class NotificationDataTablesAjaxPagination(DataTableMixin, View):
    model = Notification
    queryset = Notification.objects.all().order_by('-id')

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("edit-notification", kwargs={'pk':obj.pk})
        delete_url = reverse("delete-notification", kwargs={'pk':obj.pk})
        send_url = reverse("notification-send", kwargs={'pk':obj.pk}) 
        return f"""
                    <a href="{send_url}" title="Send" class="btn btn-warning btn-xs">
                        <i class="fa fa-bell"></i>
                    </a>
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
                Q(title__icontains=self.search) |
                Q(is_read__icontains=self.search) |
                Q(notification_type__icontains=self.search) |
                Q(description__icontains=self.search) |
                Q(is_singleuser__icontains=self.search) |
                Q(status__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables

        data = []
        for o in qs:
            # image = ''
            
            # profile_image = Notification.objects.all()
            
            # if profile_image:
            #     image = '<image src="%s" height="50" widht="50"/>' % profile_image.image.url

            data.append({
                'title': o.title,
                'is_read': self.boolean_icon(o.is_read),
                'notification_type': o.notification_type,
                'description': o.description,
                'profile': "o.profile_image",
                'is_singleuser': o.is_singleuser,
                'status': o.status,
                'actions':self._get_actions(o),
            })
        return data
    
    
    def boolean_icon(self, flag):
            if flag:
                return "<i style='color:green;' class='fa fa-check'></i>"
            return "<i style='color:red;' class='fa fa-times'></i>"

    def get(self, request, *args, **kwargs):
        context_data = self.get_context_data(request)
        return JsonResponse(context_data)