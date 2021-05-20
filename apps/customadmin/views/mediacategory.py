# -*- coding: utf-8 -*-
from customadmin.mixins import HasPermissionsMixin
from customadmin.views.generic import (
    MyNewFormsetCreateView,
    MyNewFormsetUpdateView,
    MyDeleteView,
    MyListView,
    MyLoginRequiredView,
)
from django.db.models import Q
from django.template.loader import get_template
from django_datatables_too.mixins import DataTableMixin

from customadmin.forms import (
    MediaCategoryCreationForm, 
    MediaCategoryChangeForm, 
    MediaImageCreationForm, 
    MediaImageChangeForm, 
    MediaVideoCreationForm, 
    MediaVideoChangeForm,
)
from django.shortcuts import reverse
from mediacategory_api.models import MediaCategory, MediaImage, MediaVideo
from extra_views import InlineFormSetFactory

# -----------------------------------------------------------------------------
# MediaCategory
# -----------------------------------------------------------------------------

class MediaCategoryListView(MyListView):
    """View for MediaCategory listing"""

    ordering = ["id"]
    model = MediaCategory
    queryset = model.objects.all()
    template_name = "customadmin/mediacategory/mediacategory_list.html"
    permission_required = ("customadmin.view_mediacategory",)

    def get_queryset(self):
        return self.model.objects.all().exclude(is_active=False)


class MediaImageCreateInline(InlineFormSetFactory):
    """Inline view to show Material within the Parent View"""

    model = MediaImage
    form_class = MediaImageCreationForm
    factory_kwargs = {'extra': 1, 'max_num': 100, 'can_order': False, 'can_delete': True}

class MediaVideoCreateInline(InlineFormSetFactory):
    """Inline view to show Material within the Parent View"""

    model = MediaVideo
    form_class = MediaVideoCreationForm
    factory_kwargs = {'extra': 1, 'max_num': 100, 'can_order': False, 'can_delete': True}

class MediaCategoryCreateView(MyNewFormsetCreateView):
    """View to create MediaCategory"""
    
    model = MediaCategory
    inlines = [MediaImageCreateInline, MediaVideoCreateInline]
    form_class = MediaCategoryCreationForm
    template_name = "customadmin/mediacategory/mediacategory_form.html"
    permission_required = ("customadmin.add_mediacategory",)

    def get_success_url(self):
        return reverse("customadmin:mediacategory-list")


class MediaImageUpdateInline(InlineFormSetFactory):
    """View to update Images which is a inline view"""

    model = MediaImage
    form_class = MediaImageChangeForm
    factory_kwargs = {'extra': 1, 'max_num': 100, 'can_order': False, 'can_delete': True}

class MediaVideoUpdateInline(InlineFormSetFactory):
    """View to update Video which is a inline view"""

    model = MediaVideo
    form_class = MediaVideoChangeForm
    factory_kwargs = {'extra': 1, 'max_num': 100, 'can_order': False, 'can_delete': True}

class MediaCategoryUpdateView(MyNewFormsetUpdateView):
    """View to update MediaCategory"""

    model = MediaCategory
    inlines = [MediaImageUpdateInline, MediaVideoUpdateInline]
    form_class = MediaCategoryChangeForm
    template_name = "customadmin/mediacategory/mediacategory_form.html"
    permission_required = ("customadmin.change_mediacategory",)

    def get_success_url(self):
        return reverse("customadmin:mediacategory-list")

class MediaCategoryDeleteView(MyDeleteView):
    """View to delete MediaCategory"""

    model = MediaCategory
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_mediacategory",)

    def get_success_url(self):
        return reverse("customadmin:mediacategory-list")

class MediaCategoryAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = MediaCategory
    queryset = MediaCategory.objects.all().order_by("created_at")

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("customadmin:mediacategory-update", kwargs={'pk':obj.pk})
        delete_url = reverse("customadmin:mediacategory-delete", kwargs={'pk':obj.pk})
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