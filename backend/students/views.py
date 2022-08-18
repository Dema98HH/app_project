#from django.shortcuts import render
#from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet

from .models import Stundent
from .serializers import StudentSerializer

# Create your views here.

class StudentsViewSet(ModelViewSet):
    queryset = Stundent.objects.all()
    serializer_class = StudentSerializer

    def get_serializer_class(self):
        return StudentSerializer


#def index(request):
    #model_to_dict
    #list(Students.objects.values())

    #students = Stundent.objects.all()

    #students = []

    #for student in Stundent.objects.all():
        #students.append({
           # 'name': student.name,
            #'course': student.course,
            #'rating': student.rating,
      #  })


    #return JsonResponse(students, safe=False)
