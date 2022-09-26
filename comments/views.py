from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from api_cadius.permissions import IsOwner


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    serializer_class = CommentSerializer
    queryset = Comment.objects.annotate()