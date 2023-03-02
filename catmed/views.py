from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CatSerializer
from .models import CatMed


@api_view(['GET', 'POST'])
def catmed_list(request):
    if request.method == 'GET':
        cats = CatMed.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = CatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['GET', 'PUT', 'DELETE'])
def catmed_detail(request, pk):
    cats = get_object_or_404(CatMed, pk=pk)
    if request.method == 'GET':
        serializer = CatSerializer(cats)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CatSerializer(cats, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


