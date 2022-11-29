from django.db.models import Count
from django.db.models import Avg
from django.http import Http404
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Server
from .serializers import ServerSerializer
from api_cadius.permissions import IsOwner


class ServerList(generics.ListCreateAPIView):
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Server.objects.annotate(
        comments_count=Count('comment', distinct=True),
        avg_rating=Avg('rating__rating')
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user)


class ServerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = ServerSerializer
    queryset = Server.objects.annotate(
        comments_count=Count('comment', distinct=True),
        avg_rating=Avg('rating__rating')
    ).order_by('-created_at')
