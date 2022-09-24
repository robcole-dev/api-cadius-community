from rest_framework import generics, permissions
from rest_framework.response import Response
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

