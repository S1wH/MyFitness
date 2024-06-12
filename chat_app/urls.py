from rest_framework import routers
from .views import ConversationViewSet


router = routers.DefaultRouter()
router.register('conversations', ConversationViewSet)

app_name = 'chat_app'

urlpatterns = [

]

urlpatterns += router.urls
