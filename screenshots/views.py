from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Screenshot
from .serializers import ScreenshotSerializer
from api_cadius.permissions import IsOwner


class ScreenshotList(generics.ListCreateAPIView):
    serializer_class = ScreenshotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Screenshot.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ScreenshotDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = ScreenshotSerializer
    queryset = Screenshot.objects.annotate()
