from django.urls import path
from .views import (
    CompanyCreateView,
    CompanyDeleteView,
    CompanyDetailView,
    CompanyListView,
    CompanyUpdateView,

)

app_name = 'company'
urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('create/', CompanyCreateView.as_view(), name='company-create'),
    path('<int:id>/', CompanyDetailView.as_view(), name='company-detail'),
    path('<int:id>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('<int:id>/delete/', CompanyDeleteView.as_view(), name='company-delete'),

    ]
