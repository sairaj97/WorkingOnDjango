from django import forms

from .models import Company

from rest_framework import serializers


class CompanyModelForm(forms.ModelForm):
    class Meta:
        model = Company
        fields =[
            'title',
            'content',
            'active',
        ]

class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields =[
            'title',
            'content',
            'active',
        ]