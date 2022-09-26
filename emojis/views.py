from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Emoji
from .serializers import EmojiSerializer
from api_cadius.permissions import IsOwner


class EmojiList(generics.ListCreateAPIView):
    serializer_class = EmojiSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Emoji.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)