from django.urls import path, include
from rest_framework import routers
from .views import *

#router = routers.DefaultRouter()
#router.register('', EmployeeViewSet)

urlpatterns = [
 #    path('employee/', include(router.urls)),
  #path('employee/is_active=True/', EmployeeListView.as_view()),
  path('employee/', EmployeeListView.as_view())
]