from django.urls import path
from rest_framework import routers
from .views import CoachViewSet


router = routers.DefaultRouter()
router.register('coaches', CoachViewSet)

app_name = 'users_app'

urlpatterns = [
]

urlpatterns += router.urls
