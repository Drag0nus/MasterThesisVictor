from .serializers import BoardHistorySerializer
from .models import BoardHistory
from rest_framework import viewsets


class BoardHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BoardHistory.objects.all()
    serializer_class = BoardHistorySerializer
