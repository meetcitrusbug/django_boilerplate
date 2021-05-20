# import os

# from django.db import models
# from django.dispatch import receiver
# from django.utils.translation import ugettext_lazy as _
# from mediacategory_api.models import MediaImage, MediaVideo
# from django_boilerplate.models import User


# # FOR USER PROFILE PICTURE
# @receiver(models.signals.post_delete, sender=User)
# def auto_delete_file_on_delete(sender, instance=None, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` is deleted.
#     """
    
#     if  instance and instance.profile_image:
#         if os.path.isfile(instance.profile_image.path):
#             os.remove(instance.profile_image.path)
            

# @receiver(models.signals.pre_save, sender=User)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = User.objects.get(pk=instance.pk).profile_image
#     except ValueError:
#         return False

#     if old_file :
#         new_file = instance.profile_image
#         if not old_file == new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)


# # FOR USER MEDIA IMAGES
# @receiver(models.signals.post_delete, sender=MediaImage)
# def auto_delete_file_on_delete(sender, instance=None, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` is deleted.
#     """
    
#     if  instance and instance.image:
#         if os.path.isfile(instance.image.path):
#             os.remove(instance.image.path)
            

# @receiver(models.signals.pre_save, sender=MediaImage)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = MediaImage.objects.get(pk=instance.pk).image
#     except ValueError:
#         return False

#     if old_file :
#         new_file = instance.image
#         if not old_file == new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)



# # FOR USER MEDIA VIDEOS
# @receiver(models.signals.post_delete, sender=MediaVideo)
# def auto_delete_file_on_delete(sender, instance=None, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` is deleted.
#     """
    
#     if  instance and instance.video:
#         if os.path.isfile(instance.video.path):
#             os.remove(instance.video.path)
            

# @receiver(models.signals.pre_save, sender=MediaVideo)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes old file from filesystem
#     when corresponding `MediaFile` is updated
#     with new file.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = MediaVideo.objects.get(pk=instance.pk).video
#     except ValueError:
#         return False

#     if old_file :
#         new_file = instance.video
#         if not old_file == new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)