"""
This is a view module to define list, create, update, delete views.

You can define different view properties here.
"""

from django.contrib import messages
from django.contrib.auth import get_permission_codename
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)
from django.views.generic.dates import DayArchiveView
from django.views.generic.dates import TodayArchiveView
from django.views.generic.edit import FormView
from extra_views import CreateWithInlinesView, NamedFormsetsMixin, UpdateWithInlinesView
from multi_form_view import MultiModelFormView

from django_boilerplate.mixins import HasPermissionsMixin, ModelOptsMixin, SuccessMessageMixin
from django_boilerplate.utils import admin_urlname, get_deleted_objects

MSG_CREATED = '{0} save successfully.'
MSG_UPDATED = '{0} save successfully.'
MSG_DELETED = '{0} deleted successfully.'
MSG_CANCELED = 'Data canceled successfully.'

# -----------------------------------------------------------------------------
# Generic Views
# -----------------------------------------------------------------------------


class MyView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """View with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class MyLoginRequiredView(LoginRequiredMixin, View):
    """View with LoginRequiredMixin."""

    pass


class MyTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    """TemplateView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class MyFormView(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    """FormView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class MyListView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    ListView,
):
    """ListView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    def has_permission(self):
        """Check for the permission"""
        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()

    # def get_permission_required(self):
    #     """Default to view and change perms."""
    #     # perms = super().get_permission_required()
    #     opts = self.model._meta
    #     codename_view = get_permission_codename("view", opts)
    #     codename_change = get_permission_codename("change", opts)
    #     view_perm = f"{opts.app_label}.{codename_view}"
    #     change_perm = f"{opts.app_label}.{codename_change}"
    #     perms = (view_perm, change_perm)
    #     print(perms)
    #     return perms


class MyDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    DetailView
):
    """DetailView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class MyCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    CreateView,
):
    """CreateView CBV with LoginRequiredMixin, PermissionRequiredMixin
    and SuccessMessageMixin."""

    def get_success_message(self):
        """Get success message"""
        return MSG_CREATED.format(self.model._meta.model_name).capitalize()

    def get_success_url(self):
        """Get success URL"""
        print("MyCreateView::get_success_url")
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))

    def has_permission(self):
        """Check for the permission"""

        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()


class MyUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    UpdateView,
):
    """UpdateView CBV with LoginRequiredMixin, PermissionRequiredMixin
    and SuccessMessageMixin."""

    def get_permission_required(self):
        """Default to view and change perms."""
        # perms = super().get_permission_required()
        opts = self.model._meta
        codename_view = get_permission_codename("view", opts)
        codename_change = get_permission_codename("change", opts)
        view_perm = f"{opts.app_label}.{codename_view}"
        change_perm = f"{opts.app_label}.{codename_change}"
        perms = (view_perm, change_perm)
        # print(perms)
        return perms

    def get_success_message(self):
        """Get success message"""
        return MSG_UPDATED.format(self.object._meta.model_name).capitalize()

    def get_success_url(self):
        """Get success URL"""
        print("MyUpdateView::get_success_url")
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))
        # try:
        #     return reverse(admin_urlname(opts, "list"))
        # except NoReverseMatch:
        #     return reverse(
        #         admin_urlname(opts, "update"), kwargs={"pk": self.get_object().pk}
        #     )

    def has_permission(self):
        """Check for the permission"""

        # print('----------------------------is staff------------------------------------')
        # print(self.request.user.is_staff)
        # print('----------------------------is staff------------------------------------')
        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()


class MyDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    DeleteView,
):
    """CBV to delete a model record - both Ajax and POST requests."""

    def get_success_message(self):
        """Get success message"""
        return MSG_DELETED.format(self.object._meta.model_name).capitalize()

    def get_success_url(self):
        """Get success URL"""
        print("MyDeleteView:: get_success_url")
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))

    def delete(self, request, *args, **kwargs):
        """Override delete method."""
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.get_success_message())
        if self.request.is_ajax():
            response_data = {}
            response_data["result"] = True
            response_data["message"] = self.get_success_message()
            return JsonResponse(response_data)
        return response

    def get_context_data(self, **kwargs):
        """Get deletable objects."""
        # TODO: Move to deleted objects mixin and reference self?
        ctx = super().get_context_data(**kwargs)
        # print(ctx["opts"].__dict__.keys())

        # Do some extra work here
        opts = self.model._meta

        # Populate deleted_objects, a data structure of all related objects that
        # will also be deleted.
        # deleted_objects, model_count, perms_needed, protected = self.get_deleted_objects([obj], request)
        deleted_objects, model_count, protected = get_deleted_objects([self.object])

        object_name = str(opts.verbose_name)

        # if perms_needed or protected:
        if protected:
            title = _("Cannot delete %(name)s") % {"name": object_name}
        else:
            title = _("Are you sure?")

        ctx["title"] = title
        ctx["deleted_objects"] = deleted_objects
        ctx["model_count"] = dict(model_count).items()
        ctx["protected"] = protected
        return ctx

    def has_permission(self):
        """Check for the permission"""

        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()


class MyCancelView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    DetailView,
):
    """CBV with LoginRequiredMixin, PermissionRequiredMixin
    and SuccessMessageMixin."""

    def get_success_message(self):
        """Get success message"""
        return MSG_CANCELED.format(self.object)

    def get_success_url(self):
        """Get success URL"""
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))

    def cancel(self, request, *args, **kwargs):
        """Call `cancel` method on object."""
        self.object = self.get_object()
        success_url = self.get_success_url()
        if "force" in kwargs:
            self.object.cancel(force=True)
        else:
            self.object.cancel()
        # TODO: self.request or request?
        if self.request.is_ajax():
            response_data = {}
            response_data["result"] = True
            response_data["message"] = self.get_success_message()
            return JsonResponse(response_data)
        messages.success(self.request, self.get_success_message())
        return HttpResponseRedirect(success_url)

    def post(self, request, *args, **kwargs):
        """Override POST method"""
        return self.cancel(request, *args, **kwargs)


# -----------------------------------------------------------------------------
# Formset Views
# -----------------------------------------------------------------------------


class MyNewFormsetCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    NamedFormsetsMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    CreateWithInlinesView,
):
    """CreateView CBV with CreateWithInlinesView."""

    def get_success_url(self):
        """Get success URL"""
        # TODO: Should be moved to form_valid
        messages.success(self.request, MSG_CREATED.format(self.model._meta.model_name).capitalize())
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))

    def has_permission(self):
        """Check for the permission"""

        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()


class MyNewFormsetUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    NamedFormsetsMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    UpdateWithInlinesView,
):
    """UpdateView CBV with UpdateWithInlinesView."""

    def get_success_url(self):
        """Get success URL"""
        # TODO: Should be moved to form_valid
        messages.success(self.request, MSG_UPDATED.format(self.model._meta.model_name).capitalize())
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))

    def has_permission(self):
        """Check for the permission"""

        if self.request.user.is_staff:
            return True
        else:
            return super().has_permission()

# -----------------------------------------------------------------------------
# Multi Form Views
# -----------------------------------------------------------------------------


class MyMultiModelFormView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    SuccessMessageMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    MultiModelFormView,
):
    """MultiModelFormView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    model = None
    # Object should be set within `forms_valid`
    object = None
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        """Get context data"""
        ctx = super().get_context_data(**kwargs)
        # Inject the primary object we may be editing
        ctx["object"] = self.object
        return ctx

    def get_success_url(self):
        """Get success URL"""
        print("MyMultiModelFormView::get_success_url")
        # return self.object.get_absolute_url()
        opts = self.model._meta
        return reverse(admin_urlname(opts, "list"))


# -----------------------------------------------------------------------------
# Date Views
# -----------------------------------------------------------------------------


class MyDayArchiveView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    DayArchiveView,
):
    """DayArchiveView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass


class MyTodayArchiveView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ModelOptsMixin,
    HasPermissionsMixin,
    TodayArchiveView,
):
    """TodayArchiveView CBV with LoginRequiredMixin and PermissionRequiredMixin."""

    pass
