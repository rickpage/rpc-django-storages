from django.db import models

class ImageData(models.Model):
    """
    Represents image data for an image that is best represented
    as a standalone unit
    """
    image = models.ImageField(upload_to="imagedata")
    # 0123456890123456890123456890123456890123456890123456891234
    caption = models.CharField(max_length=64, blank=True, null=True)
    # Can be used as notes about the photo, or additional details
    description = models.CharField(max_length=256, blank=True, null=True)
