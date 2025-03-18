from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Bhaiyo !")

def room(request):
    return render(request,'room.html')

# Create your views here.
