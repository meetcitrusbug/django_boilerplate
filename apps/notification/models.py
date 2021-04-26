from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

class Notification(ActivityTracking):
    TYPES_CHOICES = (
        ("OTHER", _("OTHER")),
        ("BOOKING", _("BOOKING")),
    )
    STATUS_CHOICES = (
        ("SENT", _("SENT")),
        ("PENDING", _("PENDING")),
    )
    title = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="",
        help_text=_("Notification Title"),
        verbose_name=_("Title"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("Notification Description"),
        verbose_name=_("Description"),
    )
    is_read = models.BooleanField(
        default=False,
        help_text=_("Is Notification Read?"),
        verbose_name=_("Is Notification Read?"),
    )
    notification_type = models.CharField(
        max_length=255,
        choices=TYPES_CHOICES,
        null=True,
        blank=True,
        help_text=_("Notification Type"),
        verbose_name=_("Types"),
    )
    profile_image = models.ImageField(upload_to="profile_image", default="sample.jpg", null=True,  blank=True, verbose_name=_("Profile Image"))

    is_singleuser = models.BooleanField(
        default=False,
        help_text=_("Is Single User?"),
        verbose_name=_("Is Single User?"),
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        null=True,
        blank=True,
        help_text=_("Notification Status"),
        verbose_name=_("Status"),
    )
    group = models.ForeignKey(
        "Group",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        get_user_model(),
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
        help_text=_("Group Name"),
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
        get_user_model(),
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.group_name.group_name

    class Meta:
        verbose_name = _("Group User")
        verbose_name_plural = _("Group Users")
        ordering = ["-created_at"]