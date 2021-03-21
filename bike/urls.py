from django.urls import path
from .views import (
    bike_create_view,
    bike_detail_view,
    bike_delete_view,
    bike_list_view,
    bike_update_view,

)

app_name = 'bike'
urlpatterns = [
    path('', bike_list_view, name='bike-list'),
    path('create/', bike_create_view, name='bike-list'),
    path('<int:id>/', bike_detail_view, name='bike-detail'),
    path('<int:id>/update/', bike_update_view, name='bike-update'),
    path('<int:id>/delete/', bike_delete_view, name='bike-delete'),
]