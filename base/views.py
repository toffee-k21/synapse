from django.shortcuts import render
from django.http import HttpResponse

rooms = [{'id':"1",'name':"lets explore !"},
         {'id':"2",'name':"lets code !"},
         {'id':"3",'name':"lets sing !"}]

def home(request):
    return render(request, 'base/home.html', {'rooms' : rooms})

def room(request,pk): 
    print(pk)
    for i in rooms:
        if(int(pk) == int(i['id'])):
            r = i         
    return render(request,'base/room.html', {'room' : r})

# Create your views here.
