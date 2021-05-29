from django.db import models

# ----------------------------------------------------------------------
# User Profile Model
# ----------------------------------------------------------------------


class UserProfile(models.Model):

    """This model stores the data into User Profile table in db"""

    user = models.ForeignKey(
        "django_boilerplate.User",
        on_delete=models.CASCADE,
        related_name="user_profile",
        null=True,
        blank=True,
    )
    subscription = models.ForeignKey(
        "customadmin.Plan",
        on_delete=models.CASCADE,
        related_name="user_subscription_plan",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name="Created at"
    )
    stripe_subscription_id = models.CharField(max_length=222, blank=True, null=True)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile"


    def __str__(self):
            return "{0}".format(self.user)


