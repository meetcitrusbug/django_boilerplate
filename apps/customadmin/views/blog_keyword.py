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

from customadmin.forms import BlogKeywordChangeForm, BlogKeywordCreationForm
from django.shortcuts import reverse
from Blog.models import BlogKeyword
from extra_views import InlineFormSetFactory

# -----------------------------------------------------------------------------
# BlogKeyword
# -----------------------------------------------------------------------------

class BlogKeywordListView(MyListView):
    """View for BlogKeyword listing"""

    ordering = ["id"]
    model = BlogKeyword
    queryset = model.objects.all()
    template_name = "customadmin/blog_keyword/blog_keyword_list.html"
    permission_required = ("customadmin.view_blog_keyword",)

    def get_queryset(self):
        return self.model.objects.all()

class BlogKeywordCreateView(MyCreateView):
    """View to create BlogKeyword"""
    
    model = BlogKeyword
    form_class = BlogKeywordCreationForm
    template_name = "customadmin/blog_keyword/blog_keyword_form.html"
    permission_required = ("customadmin.add_blog_keyword",)

    def get_success_url(self):
        return reverse("customadmin:blogkeyword-list")


class BlogKeywordUpdateView(MyUpdateView):
    """View to update BlogKeyword"""

    model = BlogKeyword
    form_class = BlogKeywordChangeForm
    template_name = "customadmin/blog_keyword/blog_keyword_form.html"
    permission_required = ("customadmin.change_blog_keyword",)

    def get_success_url(self):
        return reverse("customadmin:blogkeyword-list")

class BlogKeywordDeleteView(MyDeleteView):
    """View to delete BlogKeyword"""

    model = BlogKeyword
    template_name = "customadmin/confirm_delete.html"
    permission_required = ("customadmin.delete_blog_keyword",)

    def get_success_url(self):
        return reverse("customadmin:blogkeyword-list")

class BlogKeywordAjaxPagination(DataTableMixin, HasPermissionsMixin, MyLoginRequiredView):
    """Built this before realizing there is
    https://bitbucket.org/pigletto/django-datatables-view."""

    model = BlogKeyword
    queryset = BlogKeyword.objects.all()

    def _get_is_superuser(self, obj):
        """Get boolean column markup."""
        t = get_template("customadmin/partials/list_boolean.html")
        return t.render({"bool_val": obj.is_superuser})

    def _get_actions(self, obj):
        """Get action buttons w/links."""
        edit_url = reverse("customadmin:blog_keyword-update", kwargs={'pk':obj.pk})
        delete_url = reverse("customadmin:blog_keyword-delete", kwargs={'pk':obj.pk})
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