from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user =  User.objects.get(username=username)
        except:
            messages.error(request, "username not found")

        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request,user)   
            return redirect('home')
        else:
            messages.error(request, "username or password doesnt exists")

    return render(request, 'base/login_register.html')

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    return render(request, 'base/home.html', {'rooms' : rooms, 'topics': topics,'rooms_count':rooms_count})

def room(request,pk): 
    room = Room.objects.get(id=pk)
    return render(request,'base/room.html', {'room' : room})

@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room-form.html', {'form': form})

@login_required(login_url='/login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance = room)

    if request.user != room.host:
        return HttpResponse('You are not allowed to change')

    
    if request.method == 'POST':
       form = RoomForm(request.POST, instance=room)
       if form.is_valid():
           form.save()
           return redirect("home")
       
    return render(request, 'base/room-form.html', {'form': form})

@login_required(login_url='/login')
def deletRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed to change')

    if request.method == 'POST':
        room.delete()
        return redirect("home")
       
    return render(request, 'base/delete.html', {'obj': room})

