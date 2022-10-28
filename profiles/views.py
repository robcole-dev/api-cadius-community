from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from api_cadius.permissions import IsOwner


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer()


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwner]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
