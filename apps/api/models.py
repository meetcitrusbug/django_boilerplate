from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse


class User(AbstractUser):
    apple_token = models.TextField(_("Apple Token"), blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_absolute_url(self):
        return reverse("core:user-list", kwargs={"username": self.username})

    def __str__(self):
        return "{0}".format(self.username)