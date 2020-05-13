from django.shortcuts import render, redirect
from django.http import HttpResponse

from Songs.forms import Add_Album_form
from Songs.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random

def Home(request):
    data = Album.objects.all()
    d = {
        "data": data
    }
    return render(request, "index.html", d)


def Albums(request, ID):
    data = Album.objects.filter(id=ID)
    error = False
    if data:
        data = data[0]
    else:
        error = True

    d = {"id": ID, "data": data, "error": error}

    return render(request, "album.html", d)


def Songs(request, ID):
    data = Song.objects.filter(id=ID)
    error = False
    if data:
        data = data[0]
    else:
        error = True

    d = {"id": ID, "data": data, "error": error}

    return render(request, "song.html", d)


def Add_Album(request, what, Album_Id):
    if not request.user.is_authenticated:
        return redirect("Login")

    if what == "Edit":
        album = Album.objects.filter(id = Album_Id).first()
        form = Add_Album_form(request.POST or None, request.FILES or None, instance=Album)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("home")
        return render(request, "add_album.html", {"form": form})

    if what == "Delete":
        album = Album.objects.filter(id = Album_Id).first()
        album.delete()
    return redirect("home")

    if what != "Add":
        return HttpResponse("You Entered Wrong Url")

    form = Add_Album_form()
    if request.method == "POST":
        form = Add_Album_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("home")
    return render(request, "add_album.html", {"form":form})



def Add_Song(request, Album_Id):

    if request.method == "POST":
        title = request.POST["title"]
        duration = request.POST["duration"]
        poster = request.POST["poster"]
        artists = Album.objects.get(id=Album_Id)
        audio = request.POST["audio"]
        video = request.POST["video"]
        b = Song()
        b.title = title
        b.artists=artists
        b.duration = duration
        #b.artists_id =Album_Id
        b.poster = poster
        b.audio = audio
        b.video = video
        b.save()

        return redirect('albums', Album_Id)
    return render(request, "add_song.html")

def Login(request):
    if request.user.is_authenticated:
        return redirect("add_album")
    if request.method == "POST":
        un=request.POST["un"]
        ps=request.POST["ps"]
        usr=authenticate(username=un, password=ps)
        if usr:
            login(request,usr)
            return redirect("add_album")
    return render(request,"Login.html")

def Logout(request):
    logout(request)
    return redirect("Login")

def Register(request):
    error = False
    if request.method == "POST":
        d = request.POST
        name = d['name']
        un = d['un']
        ps = d['ps']
        email = d['email']
        usr = User.objects.filter(username = un)
        if not usr:
            usr = User.objects.create_user(un, email, ps)
            #a=[]
            st=int(random.randint(100,999))
            a=un+st
            usr.first_name = name
            usr.save()
            return redirect("Login")
        error = True


    return render(request, "register.html",{"error": error})
