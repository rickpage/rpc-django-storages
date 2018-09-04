from django.db import models

from base.models import WithCreator


class Photo(WithCreator):
    """
    A user-uploaded photo.
    Creator, created, description, and image field
    """
    image = models.ImageField()
    # Can be used as notes about the photo, or additional details
    description = models.CharField(max_length=256, blank=True, null=True)

class ImageData(models.Model):
    """
    Represents image data for an image that is best represented
    as a standalone unit
    """
    image = models.ImageField()
    # 0123456890123456890123456890123456890123456890123456891234
    caption = models.CharField(max_length=64, blank=True, null=True)
    # Can be used as notes about the photo, or additional details
    description = models.CharField(max_length=256, blank=True, null=True)
