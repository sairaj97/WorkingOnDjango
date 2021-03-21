"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.views import about_view, home_view
from employee.views import LoginView, LogoutView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='TRYDJANGO API Documentation')

urlpatterns = [
    path('api_documentation/', schema_view),
    path('admin/', admin.site.urls),
    path('', home_view , name='home'),
    path('about/', about_view),
    path('bike/', include('bike.urls')),
    path('company/', include('company.urls')),
    path('api/v1/', include('employee.api_urls')),
    path('api/v1/', include('poll.api_urls')),
    #path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/login/', LoginView.as_view()),
    path('api/v1/auth/logout/', LogoutView.as_view()),

]
