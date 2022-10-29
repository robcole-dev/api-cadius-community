from django.db.models import Avg
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rating
from .serializers import RatingSerializer
from api_cadius.permissions import IsOwner


class RatingList(APIView):
    serializer_class = RatingSerializer

    def get(self, request):
        rating = Rating.objects.all()
        serializer = RatingSerializer(
            rating, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RatingDetail(APIView):
    permission_classes = [IsOwner]
    serializer_class = RatingSerializer

    def get_rating(self, pk):
        try:
            rating = Rating.objects.get(pk=pk)
            self.check_object_permissions(self.request, rating)
            return rating
        except Rating.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        rating = self.get_rating(pk)
        serializer = RatingSerializer(
            rating, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        rating = self.get_rating(pk)
        serializer = RatingSerializer(
            rating, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        rating = self.get_rating(pk)
        rating.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
