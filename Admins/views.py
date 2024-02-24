from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib import messages,auth
from django.contrib.auth import login as auth_login
# from hotels.models import Hotels
from django.contrib.auth import logout
# from users.views import user_home
# from hotels.views import hotel_login
# Create your views here.

def index(request):
      return render(request,'commons/index.html')