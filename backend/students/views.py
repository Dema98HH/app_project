#from django.shortcuts import render
#from django.http import JsonResponse

from itertools import product
from rest_framework.viewsets import ModelViewSet

from .models import Stundent, Product
from .serializers import StudentSerializer, ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class StudentsViewSet(ModelViewSet):
    queryset = Stundent.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        return StudentSerializer




class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


