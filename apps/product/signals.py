import os
import uuid

from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from product.models import ProductImage

@receiver(models.signals.post_delete, sender=ProductImage)
def auto_delete_file_on_delete(sender, instance=None, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` is deleted.
    """
    
    if  instance and instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
            

@receiver(models.signals.pre_save, sender=ProductImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = ProductImage.objects.get(pk=instance.pk).image
    except ProductImage.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)