from django.core.exceptions import ValidationError
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Coach, Client
from .serializer import CoachSerializer, ClientSerializer
from .permissions import CreateOnly
from .utils import create_user


class CoachViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [IsAuthenticated | CreateOnly]

    def create(self, request, *args, **kwargs):
        try:
            user = create_user(request.data)
            request.data['user'] = user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return_data = serializer.data
            return_data.update({"token": Token.objects.get(user=user).key})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated | CreateOnly]

    def create(self, request, *args, **kwargs):
        try:
            user = create_user(request.data)
            request.data['user'] = user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return_data = serializer.data
            return_data.update({"token": Token.objects.get(user=user).key})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)
