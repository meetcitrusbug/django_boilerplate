from django.db import models
from django_boilerplate.models import ActivityTracking
from django.utils.translation import gettext as _


class MediaCategory(ActivityTracking):
    category = models.CharField(max_length=255, null=True, blank=True, default="", verbose_name=_("MediaCategory"))

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = _("MediaCategory")
        verbose_name_plural = _("MediaCategories")
        ordering = ["-created_at"]


class MediaImage(ActivityTracking):
    image = models.ImageField(upload_to="Images", null=True,  blank=True, verbose_name=_("Image"))
    category = models.ForeignKey("MediaCategory", null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _("MediaImage")
        verbose_name_plural = _("MediaImages")
        ordering = ["-created_at"]


class MediaVideo(ActivityTracking):
    video = models.FileField(upload_to="Videos", null=True,  blank=True, verbose_name=_("Video"))
    category = models.ForeignKey("MediaCategory", null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = _("MediaVideo")
        verbose_name_plural = _("MediaVideos")
        ordering = ["-created_at"]