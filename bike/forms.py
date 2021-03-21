from django import forms

from .models import Bike


class BikeForm(forms.ModelForm):
    bike_no = forms.CharField()
    bike_status = forms.IntegerField()
    last_full_maintainance_date = forms.DateField()
    device_id = forms.IntegerField()

    class Meta:
        model = Bike
        fields = [
            'bike_no',
            'bike_status',
            'last_full_maintainance_date',
            'device_id'

        ]


class RawBikeForm(forms.Form):
    bike_no = forms.CharField()
    bike_status = forms.IntegerField()
    last_full_maintainance_date = forms.DateField()
    device_id = forms.IntegerField()