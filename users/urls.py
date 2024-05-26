from django.urls import path
from rest_framework import routers
from .views import CoachViewSet, ClientViewSet


router = routers.DefaultRouter()
router.register('coaches', CoachViewSet)
router.register('clients', ClientViewSet)

app_name = 'users_app'

urlpatterns = [
]

urlpatterns += router.urls
