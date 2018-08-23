from ..models import ServerDetail
from .serializers import ServerDetailSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.app_settings import UserDetailsSerializer
class Server(APIView):
    """
    List all server of user, or create a new server.
    """
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        server = ServerDetail.objects.filter(user=request.user)
        serializer = ServerDetailSerializer(server, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=str(request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServerDeleteUpdate(APIView):
    """
    Delete and  update server.
    """
    def get_object(self, ipaddress):
        try:
            return ServerDetail.objects.get(ipaddress=ipaddress)
        except ServerDetail.DoesNotExist:
            raise Http404

    permission_classes = (IsAuthenticated,)
    def put(self, request,ipaddress,format=None):
        loadeddata= self.get_object(ipaddress)
        print(loadeddata)
        serializer = ServerDetailSerializer(loadeddata,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,ipaddress, format=None):
        loadeddata = self.get_object(ipaddress)
        loadeddata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
