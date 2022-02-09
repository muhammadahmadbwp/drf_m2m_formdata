from rest_framework import status, viewsets
from rest_framework.response import Response
from core.models import ActorsDetail
from core.serializers import ActorsSerializer, GetActorsSerializer
from rest_framework.parsers import (JSONParser, MultiPartParser, FormParser, FileUploadParser)

# Create your views here.

class ActorsViewSet(viewsets.ViewSet):

    parser_classes = [JSONParser, MultiPartParser, FormParser, FileUploadParser]

    def get_queryset(self, request):
        queryset = ActorsDetail.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        serializer = GetActorsSerializer(queryset, many=True)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ActorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"actor created successfully"}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = ActorsDetail.objects.get(pk=pk)
        serializer = ActorsSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return Response({"data":data, "success":True, "message":"actor updated successfully"}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = ActorsDetail.objects.get(pk=pk)
        serializer = GetActorsSerializer(queryset)
        data = serializer.data
        return Response({"data":data, "success":True, "message":"data found"}, status=status.HTTP_200_OK)