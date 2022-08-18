from django.urls import path
#from .views import index
from rest_framework import routers
from . import views

from .views import *


router = routers.DefaultRouter()
router.register('students', StudentsViewSet)

urlpatterns = router.urls

#urlpatterns = [
#   path('students/', views.index)
#]