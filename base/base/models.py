from django.conf import settings
from django.db import models


class WithCreator(models.Model):

    created = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,)

    class Meta:
        abstract = True