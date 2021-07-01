from django.contrib.auth import get_user_model
from django.db import models


class Cookie(models.Model):
    name = models.CharField(max_length=256)
    baker = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self):
        return self.name
