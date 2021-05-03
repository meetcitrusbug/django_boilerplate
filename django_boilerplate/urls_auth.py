"""
You can write your URL patterns here,

This URL patterns follow auth namespace.
"""

from django.contrib.auth import views as auth_views
from django.urls import path, re_path

# -----------------------------------------------------------------------
# Auth URL patterns
# -----------------------------------------------------------------------

app_name = "auth"

urlpatterns = [
    # Login / Logout
    path(
        "login/",
        auth_views.LoginView.as_view(),
        name="auth_login"),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        {'next_page': 'core:auth_login'},  # redirect user
        name="auth_logout",
    ),

    # Password Change
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(),
        name="auth_password_change"
    ),

    path(
        "password/change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done"
    ),

    # Password reset
    path(
        "password/reset/",
        auth_views.PasswordResetView.as_view(),
        name="reset_password"
    ),

    re_path(
        r"^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

    path(
        "password/reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),

    path(
        "password/reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"
    ),
]
