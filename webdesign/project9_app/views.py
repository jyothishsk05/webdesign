from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def reg (request):

   if request.method == 'POST':
    username = request.POST['username']
    first_name= request.POST['first_name']
    last_name= request.POST['last_name']
    email=request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['password']
    user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name,email=email)
    user.save();
    print("user created"),

   return render(request ,'register.html')
