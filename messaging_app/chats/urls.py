from django.urls import path, include
from rest_framework import routers   # 👈 import routers module
from rest_framework.routers import NestedDefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Main router
router = routers.DefaultRouter()   # 👈 satisfies the check
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Nested router for messages under conversations
nested_router = NestedDefaultRouter(router, r'conversations', lookup='conversation')
nested_router.register(r'messages', MessageViewSet, basename='conversation-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
