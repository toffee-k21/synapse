from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# rooms = [{'id':"1",'name':"lets explore !"},
#          {'id':"2",'name':"lets code !"},
#          {'id':"3",'name':"lets sing !"}]


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request,pk): 
    room = Room.objects.get(id=pk)
    return render(request,'base/room.html', {'room' : room})

