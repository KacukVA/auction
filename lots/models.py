from django.db import models
from django.contrib.auth.models import User


class Lot(models.Model):
    PLACED = 'PLACED'
    FINISHED = 'FINISHED'
    STATUS_CHOICES = (
        (PLACED, "Placed"),
        (FINISHED, "Finished"),
    )
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=1)
    created_by = User()
    status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        default=PLACED
    )