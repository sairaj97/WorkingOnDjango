from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)

from .forms import CompanyModelForm
from .models import Company
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import FilterSet
from django_filters import rest_framework as filters


class CompanyCreateView(CreateView):
    template_name = 'company_create.html'
    form_class = CompanyModelForm
    queryset = Company.objects.all()  # <blog>/<modelname>_list.html

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #    return '/'


class CompanyListView(ListView):
    template_name = 'company_list.html'
    queryset = Company.objects.all()  # <blog>/<modelname>_list.html


class CompanyDetailView(DetailView):
    template_name = 'company_detail.html'

    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Company, id=id_)


class CompanyUpdateView(UpdateView):
    template_name = 'company_create.html'
    form_class = CompanyModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Company, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class CompanyDeleteView(DeleteView):
    template_name = 'company_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Company, id=id_)

    def get_success_url(self):
        return reverse('company:company-list')


