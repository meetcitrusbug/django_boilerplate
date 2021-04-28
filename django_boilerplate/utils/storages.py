"""
Define AWS storage related stuff here.
"""

from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):
    """
    This is to define location & permission for static files in AWS S3 service.
    """
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):
    """
    This is to define location & permission for media files in AWS S3 service.
    """
    location = "media"
    file_overwrite = False
