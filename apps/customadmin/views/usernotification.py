# -*- coding: utf-8 -*-
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView,
)
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from customadmin.forms import UserNotificationChangeForm, UserNotificationCreationForm
from django.shortcuts import reverse

from notification.models import UserNotification

# -----------------------------------------------------------------------------
# UserNotification
# -----------------------------------------------------------------------------

class UserNotificationListView(MyListView):
    """View for UserNotification listing"""

    ordering = ["id"]
    model = UserNotification
    queryset = model.objects.all()
    template_name = "customadmin/usernotification/usernotification_list.html"
    permission_required = ("customadmin.view_usernotification",)

    def get_queryset(self):
        return self.model.objects.all().exclude(is_active=False)

class UserNotificationCreateView(MyCreateView):
    """View to create UserNotification"""

    model = UserNotification
    form_class = UserNotificationCreationForm
    template_name = "customadmin/usernotification/usernotification_form.html"
    permission_required = ("customadmin.add_usernotification",)

    def get_success_url(self):
        return reverse("customadmin:usernotification-list")

class UserNotificationUpdateView(MyUpdateView):
    """View to update UserNotification"""

    model = UserNotification
    form_class = UserNotificationChangeForm
    template_name = "customadmin/usernotification/usernotification_form.html"
    permission_required = ("customadmin.change_usernotification",)

    def get_success_url(self):
        return reverse("customadmin:usernotification-list")

class UserNotificationDeleteView(MyDeleteView):
    """View to delete UserNotification"""

    model = UserNotification
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_usernotification",)

    def get_success_url(self):
        return reverse("customadmin:usernotification-list")

class UserNotificationAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = UserNotification
    queryset = UserNotification.objects.all().order_by("created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("customadmin:usernotification-update", kwargs={'pk':obj.pk})
        delete_url = reverse("customadmin:usernotification-delete", kwargs={'pk':obj.pk})
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