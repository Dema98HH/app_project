from django.urls import path, include
#from .views import index
from rest_framework import routers
from . import views

from .views import *


#router = routers.DefaultRouter()
#router.register('students', StudentsViewSet)

#urlpatterns = router.urls



urlpatterns = [
    path('latest-products/', views.LatestProductsList.as_view())
]







#urlpatterns = [
#   path('students/', views.index)
#]