from django.db import models
from django.utils import timezone

from Board.models import Board

# Create your models here.

STATION_CHOICES = [(str(i), 'Station%s' % i) for i in range(0, 5)]
STATUS_CHOICES = (
    (1, 'PASS'),
    (2, 'FAIL')
)


class BoardHistory(models.Model):
    serial_number = models.ForeignKey(Board, on_delete=models.CASCADE)
    station = models.CharField(choices=STATION_CHOICES,
                               default=None,
                               max_length=100)
    status = models.CharField(choices=STATUS_CHOICES,
                              max_length=4)
    date = models.DateTimeField(default=timezone.now)
