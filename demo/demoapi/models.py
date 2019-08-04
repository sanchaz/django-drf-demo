from django.conf import settings
from django.db import models

# Create your models here.


class DemoModel(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    field1 = models.CharField(
        max_length=20,
        unique=True,
    )
    field2 = models.BooleanField(
        default=True,
    )
