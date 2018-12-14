from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('SerialNumber', 'ProductName', 'birth_date', 'total_creation_time', 'history')