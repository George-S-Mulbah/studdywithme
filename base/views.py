from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms  import RoomForm
from .models import Room
# Create your views here.

# rooms = [
#     {'id':1 ,'name':'Learn Python'},
#     {'id':2 ,'name':'The LiberianStack'},
#     {'id':3 ,'name':'Learn Design'}
# ]
def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request,'base/room.html',context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form.as_p}
    return render(request,'base/room_form.html',context)

def updateRoom(request,pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)
  if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
  context={'form':form}
  return  render(request,'base/room_form.html',context)