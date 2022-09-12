from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Server
from .serializers import ServerSerializer


class ServerList(APIView):
    serializer_class = ServerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request):
        servers = Server.objects.all()
        serializer = ServerSerializer(servers, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ServerSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

