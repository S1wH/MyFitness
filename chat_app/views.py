from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.db.models import Q
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from users.models import User
from .models import Conversation
from .serializers import ConversationSerializer, ConversationListSerializer


class ConversationViewSet(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.ListModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            User.objects.get(id=data.coach)
        except ObjectDoesNotExist:
            return Response(f'Тренера с id {data.coach} не существует', status=status.HTTP_400_BAD_REQUEST)
        try:
            User.objects.get(id=data.client)
        except ObjectDoesNotExist:
            return Response(f'Клиента с id {data.client} не существует', status=status.HTTP_400_BAD_REQUEST)
        try:
            conv = Conversation.objects.filter(coach=data.coach, client=data.client)
            if conv.exists():
                return Response('Такой чат уже существует', status=status.HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.data.user
        conversation_list = Conversation.objects.filter(Q(coach=user) | Q(client=user))
        serializer = ConversationListSerializer(instance=conversation_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
