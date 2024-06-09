from django.urls import path
from rest_framework import routers
from .views import UserViewSet, EmailVerificationView, CoachViewSet, ClientViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('coaches', CoachViewSet)
router.register('clients', ClientViewSet)

app_name = 'users_app'

urlpatterns = [
    path('verify_email/', EmailVerificationView.as_view(), name='verify-email'),
]

urlpatterns += router.urls
