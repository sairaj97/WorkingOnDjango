from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .forms import BikeForm, RawBikeForm

from .models import Bike
# Create your views here.
def bike_detail_view(request, id=id):
    obj = Bike.objects.get(id=id)
    #context = {
    #    'bike_no': obj.bike_no,
    #    'bike_status': obj.bike_status
    #}
    context = {"object": obj}
    return  render(request, "bike/bike_detail.html", context)

def bike_create_view(request):
   form = BikeForm(request.POST or None)
   if form.is_valid():
       form.save()
       form = BikeForm()
   context = {
       'form': form
    }
   return render(request, "bike/bike_create.html", context)



def bike_update_view(request, id=id):
    obj = get_object_or_404(Bike, id=id)
    form = BikeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "bike/bike_create.html", context)

def bike_list_view(request):
    #qs = Bike.objects.all() # list of objects
    #qs_json = serializers.serialize('json', qs)
    #return HttpResponse(qs_json, content_type='application/json')
    #context = {
    #    "object_list": queryset
    #}
    #return render(request, "bike/bike_list.html", context)
    data = list(Bike.objects.values()) # wrap in list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})



def bike_delete_view(request, id):
    obj = get_object_or_404(Bike, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "bike/bike_delete.html", context)