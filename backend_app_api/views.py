from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from .serializers import *

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def list(self, request):
        temp_obj = Image.objects.all()
        serializer = ImageSerializer(temp_obj, many=True)
        if serializer.data:
            return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        
    # def create(self, request):
    #     serializer = ImageSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
    #     else:
    #         return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)           

class UserHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer

    def list(self, request):
        if 'author_id' in self.request.GET:   
            temp_obj = UserHistory.objects.filter(author = request.GET["author_id"]).order_by('-id')
            serializer = UserHistorySerializer(temp_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)
        else:
            temp_obj = UserHistory.objects.all().order_by('-id')
            serializer = UserHistorySerializer(temp_obj, many=True)
            if serializer.data:
                return Response({"status": "success", "data": {'items': serializer.data}}, status=status.HTTP_200_OK)
            else:
                return Response({"status":"Record Not Available"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"Record Added Successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)       
    