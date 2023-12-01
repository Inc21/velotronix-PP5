from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """ Store static files in AWS S3 bucket """
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """ Store media files in AWS S3 bucket """
    location = settings.MEDIAFILES_LOCATION
