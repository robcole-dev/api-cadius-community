from django.db.models import Count
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from api_cadius.permissions import IsOwner


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        server_count=Count('author__server', distinct=True)
    ).order_by('-created_date')
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Profile.objects.annotate(
        server_count=Count('author__server', distinct=True)
    ).order_by('-created_date')
    serializer_class = ProfileSerializer
