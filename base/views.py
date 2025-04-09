from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    return render(request, 'base/home.html', {'rooms' : rooms, 'topics': topics,'rooms_count':rooms_count})

def room(request,pk): 
    room = Room.objects.get(id=pk)
    return render(request,'base/room.html', {'room' : room})

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room-form.html', {'form': form})

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)
    
    if request.method == 'POST':
       form = RoomForm(request.POST, instance=room)
       if form.is_valid():
           form.save()
           return redirect("home")
       
    return render(request, 'base/room-form.html', {'form': form})

def deletRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect("home")
       
    return render(request, 'base/delete.html', {'obj': room})

