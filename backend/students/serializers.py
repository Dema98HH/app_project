from dataclasses import fields
from rest_framework.serializers import ModelSerializer

from .models import Stundent, Product, Category



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Stundent
        fields = ['id', 'name', 'course', 'rating']



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        )

class StudentsSerializer(ModelSerializer):
    class Meta:
        model = Stundent
        fields = (
            "name",
            "course",
            "rating"
        )




