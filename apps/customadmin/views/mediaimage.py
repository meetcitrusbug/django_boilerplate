# -*- coding: utf-8 -*-
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyCreateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
    MyUpdateView
)
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from customadmin.forms import MediaImageCreationForm, MediaImageChangeForm
from django.shortcuts import reverse
from mediacategory_api.models import MediaImage

# -----------------------------------------------------------------------------
# MediaImage
# -----------------------------------------------------------------------------

class MediaImageListView(MyListView):
    """View for MediaImage listing"""

    ordering = ["id"]
    model = MediaImage
    queryset = model.objects.all()
    template_name = "customadmin/mediaimage/mediaimage_list.html"
    permission_required = ("customadmin.view_mediaimage",)

    def get_queryset(self):
        return self.model.objects.all().exclude(is_active=False)

class MediaImageCreateView(MyCreateView):
    """View to create MediaImage"""
    
    model = MediaImage
    form_class = MediaImageCreationForm
    template_name = "customadmin/mediaimage/mediaimage_form.html"
    permission_required = ("customadmin.add_mediaimage",)

    def get_success_url(self):
        return reverse("customadmin:mediaimage-list")

class MediaImageUpdateView(MyUpdateView):
    """View to update MediaImage"""

    model = MediaImage
    form_class = MediaImageChangeForm
    template_name = "customadmin/mediaimage/mediaimage_form.html"
    permission_required = ("customadmin.change_mediaimage",)

    def get_success_url(self):
        return reverse("customadmin:mediaimage-list")

class MediaImageDeleteView(MyDeleteView):
    """View to delete MediaImage"""

    model = MediaImage
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_mediaimage",)

    def get_success_url(self):
        return reverse("customadmin:mediaimage-list")

class MediaImageAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = MediaImage
    queryset = MediaImage.objects.all().order_by("created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("customadmin:mediaimage-update", kwargs={'pk':obj.pk})
        delete_url = reverse("customadmin:mediaimage-delete", kwargs={'pk':obj.pk})
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