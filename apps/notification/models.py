from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from customadmin.models import User

class Notification(ActivityTracking):
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        verbose_name=_("Title"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
    )
    is_read = models.BooleanField(
        default=False,
        verbose_name=_("Is Notification Read?"),
    )
    is_singleuser = models.BooleanField(
        default=False,
        verbose_name=_("Is Single User?"),
    )
    group = models.ForeignKey(
        "Group",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "customadmin.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")
        ordering = ["-created_at"]


class Group(ActivityTracking):
    group_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        verbose_name=_("Name"),
    )
    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")
        ordering = ["-created_at"]


class GroupUser(ActivityTracking):
    group_name = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE
        )
    user = models.ForeignKey(
        "customadmin.User",
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.group_name.group_name

    class Meta:
        verbose_name = _("Group User")
        verbose_name_plural = _("Group Users")
        ordering = ["-created_at"]

class UserNotification(ActivityTracking):
    user = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        verbose_name=_("User"),
    )
    notification = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        verbose_name=_("Notification"),
    )
    read = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _("User Notification")
        verbose_name_plural = _("User Notifications")
        ordering = ["-created_at"]