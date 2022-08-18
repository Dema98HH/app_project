from rest_framework.serializers import ModelSerializer

from .models import Stundent



class StudentSerializer(ModelSerializer):
    class Meta:
        model = Stundent
        fields = ['id', 'name', 'course', 'rating']


