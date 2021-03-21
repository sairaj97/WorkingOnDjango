
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs): # *args, **kwargs
    my_context = {"my_text": "this is about us",
                  "my_number": 123,
                  "my_list": [123, 345, 5667, "abc"]
                  }
    return render(request, "about.html", my_context)