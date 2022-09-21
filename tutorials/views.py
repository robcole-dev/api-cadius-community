from django.http import Http404
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tutorial
from .serializers import TutorialSerializer


class TutorialList(APIView):
    serializer_class = TutorialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        tutorial = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorial, many=True, context={'request': request})
        return Response(serializer.data)