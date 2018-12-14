from rest_framework import serializers
from .models import BoardHistory


class BoardHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardHistory
        fields = ('serial_number', 'station', 'status', 'date')
