from django.shortcuts import render
from django.http import HttpResponse

rooms = [{'id':"1",'name':"lets explore !"},
         {'id':"2",'name':"lets code !"},
         {'id':"3",'name':"lets sing !"}]

def home(request):
    return render(request, 'base/home.html')

def room(request):
    return render(request,'base/room.html', {'rooms' : rooms})

# Create your views here.
