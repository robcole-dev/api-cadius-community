from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Server
from .serializers import ServerSerializer
from api_cadius.permissions import IsOwner


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

class ServerDetail(APIView):
    permission_classes = [IsOwner]
    serializer_class = ServerSerializer

    def get_server(self, pk):
        try:
            server = Server.objects.get(pk=pk)
            self.check_object_permissions(self.request, server)
            return server
        except Server.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        server = self.get_server(pk)
        serializer = ServerSerializer(
            server, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        server = self.get_server(pk)
        serializer = ServerSerializer(
            server, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        server = self.get_server(pk)
        server.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

