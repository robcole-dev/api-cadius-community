from django.http import Http404
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tutorial
from .serializers import TutorialSerializer
from api_cadius.permissions import IsOwner


class TutorialList(generics.ListCreateAPIView):
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tutorial.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = TutorialSerializer
    queryset = Tutorial.objects.annotate()

