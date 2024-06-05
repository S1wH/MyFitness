from django.core.exceptions import ValidationError, ObjectDoesNotExist
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, generics, mixins, views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Coach, Client, ActivationCode, User
from .serializer import CoachSerializer, ClientSerializer, UserSerializer
from .permissions import CreateOnly
from .utils import create_user
from myfitness.celery import send_mail


# class CoachViewSet(viewsets.ModelViewSet):
#     queryset = Coach.objects.all()
#     serializer_class = CoachSerializer
#     permission_classes = [IsAuthenticated | CreateOnly]
#
#     def create(self, request, *args, **kwargs):
#         try:
#             user = create_user(request.data)
#             request.data['user'] = user.id
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             return_data = serializer.data
#             return_data.update({"token": Token.objects.get(user=user).key})
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except ValidationError as e:
#             return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)


# class ClientViewSet(viewsets.ModelViewSet):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     permission_classes = [IsAuthenticated | CreateOnly]
#
#     def create(self, request, *args, **kwargs):
#         try:
#             # user = create_user(request.data)
#             # request.data['user'] = user.id
#             serializer = UserSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             self.perform_create(serializer)
#             user = User.objects.get(email=request.data['email'])
#             return_data = serializer.data
#             return_data.update({"token": Token.objects.get(user=user).key})
#             code = ActivationCode.objects.create(user=user)
#             send_mail(user.id, code.code)
#             return Response(return_data, status=status.HTTP_201_CREATED)
#         except ValidationError as e:
#             return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [CreateOnly | IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            user = User.objects.get(email=request.data['email'])
            return_data = serializer.data
            return_data.update({"token": Token.objects.get(user=user).key})
            code = ActivationCode.objects.create(user=user)
            send_mail.delay(user.id, code.code)
            return Response(return_data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)


class EmailVerificationView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="verification for user with email code", responses={400: ''},
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['code'],
                             properties={
                                 'code': openapi.Schema(type=openapi.TYPE_STRING)
                             },
                         ))
    def post(self, request):
        code = request.data.get('code', None)
        if not code:
            return Response('Код подтверждения не был указан', status=status.HTTP_400_BAD_REQUEST)
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if not token:
            return Response('Токен не был указан', status=status.HTTP_400_BAD_REQUEST)
        try:
            token = token.split(' ')[-1]
            user = Token.objects.get(key=token).user
            user_code = user.user_code
            if code != user_code.code:
                return Response('Указан неверный код', status=status.HTTP_400_BAD_REQUEST)
            user.is_verified = True
            user.save()
            user_code.delete()
        except ObjectDoesNotExist as e:
            return Response(repr(e), status=status.HTTP_400_BAD_REQUEST)
        return Response({'code': code}, status=status.HTTP_200_OK)
