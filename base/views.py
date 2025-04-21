from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if(request.method == 'POST'):
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user =  User.objects.get(email=email)
        except:
            messages.error(request, "username not found")

        user = authenticate(request, email=email, password=password) 

        if user is not None:
            login(request,user)   
            return redirect('home')
        else:
            messages.error(request, "username or password doesnt exists")

    context = {'page':page}    

    return render(request, 'base/login_register.html', context)

def registerUser(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'An error has occured')
    return render(request,'base/login_register.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    q = request.GET.get('q', '')
    # q = request.GET.get('q') if request.GET.get('q') != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))
    topics = Topic.objects.all()
    rooms_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    return render(request, 'base/home.html', {'rooms' : rooms, 'topics': topics,'rooms_count':rooms_count, 'room_messages': room_messages})

def room(request,pk):
    room = Room.objects.get(id=pk)
    room_messages = room.messages.all()
    participants = room.participants.all()

    if request.method == 'POST':
        room_messages = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    return render(request,'base/room.html', {'room' : room, 'room_messages':room_messages, 'participants': participants})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user,'rooms': rooms, 'room_messages':room_messages,'topics':topics}
    return render(request, 'base/profile.html', context)
 
@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
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
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.user != room.host:
        return HttpResponse('You are not allowed to change')

    if request.method == 'POST':
        room.delete()
        return redirect("home")
       
    return render(request, 'base/delete.html', {'obj': room})


@login_required(login_url='/login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('You are not allowed to change')

    if request.method == 'POST':
        message.delete()
        return redirect('home')
       
    return render(request, 'base/delete.html', {'obj': message})

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm( instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})