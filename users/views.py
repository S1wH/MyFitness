from rest_framework import generics, status, viewsets
from .models import Coach
from .serializer import CoachSerializer


class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
