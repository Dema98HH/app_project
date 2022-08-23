#from django.shortcuts import render
#from django.http import JsonResponse

from itertools import product
from rest_framework.viewsets import ModelViewSet

from .models import Stundent, Product
from .serializers import StudentsSerializer, ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class StundentsList(APIView):
    def get(self, request, format=None):
        students = Stundent.objects.all()
        serializer = StudentsSerializer(students, many=True)
        return Response(serializer.data)


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


