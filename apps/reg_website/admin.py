from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import AccountUpdateForm, AccountCreationForm
from django.utils.translation import ugettext_lazy as _

# Register your models here.


class UserAdmin(UserAdmin):
    form = AccountUpdateForm
    add_form = AccountCreationForm

    list_per_page = 10
    list_display = ["pk", "email", "username",]

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "phone",
                    "address",
                    "is_active",
                    "is_staff",
                    "profile_image",
                    "email_verified",
                    "phone_verified",
                    "password_reset_link",
                    "otp_number",

                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.save()
        return instance

admin.site.register(User, UserAdmin)