from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer, LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer



class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        django_logout(request)
        return Response(status=204)


class EmployeeFilter(FilterSet):
    is_active = filters.CharFilter('is_active')
    designation = filters.CharFilter('profile__designation')
    min_salary = filters.CharFilter(method="filter_by_min_salary")
    max_salary = filters.CharFilter(method="filter_by_max_salary")

    class Meta:
        model = User
        fields = ('is_active', 'designation', 'username',)

    def filter_by_min_salary(self, queryset, name, value):
        queryset = queryset.filter(profile__salary__gt=value)
        return queryset

    def filter_by_max_salary(self, queryset, name, value):
        queryset = queryset.filter(profile__salary__lt=value)
        return queryset


class EmployeeListView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields = ('is_active', 'profile__designation', )
    filter_class = EmployeeFilter

    ordering_fields = ('is_active', 'username')
    ordering = ('username',)
    search_fields = ('username', 'first_name')


    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     active = self.request.query_params.get('is_active', '')
    #     if active:
    #         if active == "False":
    #             active = False
    #         elif active == "True":
    #             active = True
    #         else:
    #             return queryset
    #         return queryset.filter(is_active=active)
    #     return queryset


