from django.db.models import Count
from django.db.models import Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Server
from .serializers import ServerSerializer
from api_cadius.permissions import IsOwner


class ServerList(generics.ListCreateAPIView):
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Server.objects.annotate(
        avg_rating=Avg('rating__rating')
    ).order_by('-created_at')
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'author_id__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = ServerSerializer
    queryset = Server.objects.annotate(
        avg_rating=Avg('rating__rating')
    ).order_by('-created_at')
