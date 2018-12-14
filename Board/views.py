from .serializers import BoardSerializer
from .models import Board
from rest_framework import viewsets


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
