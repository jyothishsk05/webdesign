from django.shortcuts import render
from .models import place, Place


# Create your views here.

def page1(request):
  obj= Place.objects.all()

  return render(request,"index.html",{'result': obj})
