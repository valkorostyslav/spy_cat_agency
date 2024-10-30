from rest_framework import viewsets
from cats.serializers import CatSerializer
from rest_framework import status
from rest_framework.response import Response
from cats.models import Cat

# Create your views here.

class CatViewSet(viewsets.ViewSet):
    
    def create(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            cat = Cat.objects.get(pk=pk)
            serializer = CatSerializer(cat)
            return Response(serializer.data)
        except Cat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk=None):
        try:
            cat = Cat.objects.get(pk=pk)
            serializer = CatSerializer(cat, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Cat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk=None):
        try:
            cat = Cat.objects.get(pk=pk)
            cat.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cat.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)