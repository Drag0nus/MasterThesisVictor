from uuid import uuid4

from django.db import models

# Create your models here.
from django.utils import timezone


class Board(models.Model):
    SerialNumber = models.CharField(default=uuid4,
                                    primary_key=True,
                                    max_length=10)
    ProductName = models.CharField(max_length=100, default=None)
    birth_date = models.DateTimeField(default=timezone.now)
    total_creation_time = models.IntegerField(null=False)
    history = models.TextField(max_length=300)
