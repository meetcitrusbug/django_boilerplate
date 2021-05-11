# -*- coding: utf-8 -*-
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
    MyDetailView,
)
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from customadmin.forms import NotificationChangeForm, NotificationCreationForm
from django.shortcuts import reverse, render
from notification.models import Notification, Group, GroupUser
from customadmin.models import User

from pyfcm import FCMNotification
from django.views import View
from django.conf import settings


# -----------------------------------------------------------------------------
# Notification
# -----------------------------------------------------------------------------

class NotificationDetailView(MyDetailView):
    template_name = "customadmin/notification/notification_detail.html"
    context = {}

    def get(self, request, pk):
        self.context['notification_detail'] = Notification.objects.filter(pk=pk).first()
        return render(request, self.template_name, self.context)
        
class NotificationListView(MyListView):
    """View for Notification listing"""

    ordering = ["id"]
    model = Notification
    queryset = model.objects.all()
    template_name = "customadmin/notification/notification_list.html"
    permission_required = ("customadmin.view_notification",)

    def get_queryset(self):
        return self.model.objects.all().exclude(is_active=False)

class NotificationCreateView(MyCreateView):
    """View to create Notification"""

    model = Notification
    form_class = NotificationCreationForm
    template_name = "customadmin/notification/notification_form.html"
    permission_required = ("customadmin.add_notification", )
    
    def get_success_url(self):
        flag = NotificationSendView.send(self.request, self.object.pk)
        return reverse("customadmin:notification-list")

class NotificationUpdateView(MyUpdateView):
    """View to update Notification"""

    model = Notification
    form_class = NotificationChangeForm
    template_name = "customadmin/notification/notification_form.html"
    permission_required = ("customadmin.change_notification",)

    def get_success_url(self):
        flag = NotificationSendView.send(self.request, self.object.pk)
        return reverse("customadmin:notification-list")

class NotificationDeleteView(MyDeleteView):
    """View to delete Notification"""

    model = Notification
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_notification",)

    def get_success_url(self):
        return reverse("customadmin:notification-list")

class NotificationAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = Notification
    queryset = Notification.objects.all().order_by("created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("customadmin:notification-update", kwargs={'pk':obj.pk})
        delete_url = reverse("customadmin:notification-delete", kwargs={'pk':obj.pk})
        return f"""
                    <a href="{edit_url}" title="Edit" class="btn btn-primary btn-xs">
                        <i class="fa fa-pencil"></i>
                    </a>
                    <a data-title="{delete_url}" title="Delete" href="{delete_url}" class="btn btn-danger btn-xs btn-delete">
                        <i class="fa fa-trash"></i>
                    </a>
                """

    def filter_queryset(self, qs):
        """Return the list of items for this view."""
        # If a search term, filter the query
        if self.search:
            return qs.filter(
                Q(username__icontains=self.search)
                | Q(first_name__icontains=self.search)
                | Q(last_name__icontains=self.search)
                # | Q(state__icontains=self.search)
                # | Q(year__icontains=self.search)
            )
        return qs

    def prepare_results(self, qs):
        # Create row data for datatables
        data = []
        for o in qs:
            data.append(
                {
                    "username": o.username,
                    "first_name": o.first_name,
                    "last_name": o.last_name,
                    "is_superuser": self._get_is_superuser(o),
                    # "modified": o.modified.strftime("%b. %d, %Y, %I:%M %p"),
                    "actions": self._get_actions(o),
                }
            )
        return data

class NotificationSendView(View):
    def send(request, pk):
        notification = Notification.objects.get(pk=pk)
        message_title = notification.title
        message_body = notification.description
        api_key = settings.FIREBASE_API_KEY
        
        if notification.is_singleuser == False:
            group_name = Group.objects.get(pk=notification.group.pk)
            users = GroupUser.objects.filter(group_name=group_name)
            user_objects = []
            for i in users:
                user_objects.append(i.user)
            registration_ids = []
            for i in user_objects:
                registration_ids.append(i.credentials)

            push_service = FCMNotification(api_key=api_key)
            result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

        else:
            registration_id = notification.user.credentials

            push_service = FCMNotification(api_key=api_key)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


        flag = False
        if result['success'] > 0:
            flag = True
            message = "Notification sent successfully!"
        else:
            message = "Notification isn't sent successfully!"
        
        return flag