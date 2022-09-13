from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rating
from .serializers import RatingSerializer
from api_cadius.permissions import IsOwner


class RatingList(APIView):
    serializer_class = RatingSerializer

    def get(self, request):
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = RatingSerializer(rating, many=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
