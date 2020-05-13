import json

import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.utils.timezone import now
from Movie.forms import Add_Movie_form, Add_Starcast_form
from Movie.models import *
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
import requests

import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'

headers = { "X-Api-Key": "85fa69f496dec0b77cf2f538b3ef5f8e",
            "X-Auth-Token": "99cc1530aad3f42e6fcf244ee1c9d644"}



def Movie_Home(request):

    movies = MovieDetails.objects.all()
    movies1 = MovieDetails.objects.order_by('-rating')
    d = {
        "movies": movies,"movies1": movies1
    }
    return render(request,"movie/index.html",d)

def Movie_Contact(request):
    return render(request,"movie/contact.html")

def MovieList(request):
    cat=Movie_Category.objects.all()
    movies=MovieDetails.objects.all()
    d={
        "category":cat, "movies":movies
    }
    return render(request,"movie/movie_category.html",d)

@login_required
def Movie_Details(request, m_id):
    data=MovieDetails.objects.filter(id=m_id).first()
    data1=MovieDetails.objects.filter(director=data.director)
    #cast=StarCast.objects.filter(id=m_id)
    d={
        "data":data,"data1":data1, "id":m_id #, "cast":cast
    }
    #return HttpResponse("Your movie id is"+str(m_id))
    return render(request,"movie/movie_single.html",d)

def Login(request):
    if request.user.is_authenticated:
        return redirect("MyMovie:movie_home")

    error=False
    if request.method == "POST":
        un = request.POST["un"]
        ps = request.POST["ps"]
        usr = authenticate(username = un, password = ps)

        if usr:
            login(request, usr)
            return redirect("MyMovie:movie_home")
        error=True
    return render(request, "movie/login.html",{"error":error})


def Logout(request):
    logout(request)
    return redirect("MyMovie:login")

def Register(request):
    if request.user.is_authenticated:
        return redirect("MyMovie:movie_home")

    error = False
    if request.method == "POST":
        d = request.POST
        name = d['name']
        un = d['un']
        ps = d['ps']
        email = d['email']
        number= d['number']
        usr = User.objects.filter(username = un)
        if not usr:
            usr = User.objects.create_user(un, email, ps)
            usr.first_name = name
            usr.save()
            Movie_users.objects.create(usr=usr, name=name, number=number)
            return redirect("MyMovie:login")
        error = True

    return render(request, "movie/register.html", {"error":error})

def Movie_Booking(request, m_id):
    movie = MovieDetails.objects.filter(id=m_id).first()
    st=ShowTime.objects.filter(movie=movie).order_by("talkies")
    Dates = []
    ShowTime1 = []

    today = datetime.date.today()
    for i in range(0, 5):
        Dates.append(today + timedelta(days=i))

    for d in Dates:
        temp = []
        TempSt = []
        talkies = ""
        for i in st:
            if d == i.date:
                if i.talkies.name != talkies:
                    if len(talkies) > 2:
                        TempSt.append((talkies, temp))
                    talkies = i.talkies.name
                    temp = []
                    temp.append(i)
                else:
                    temp.append(i)
        TempSt.append((talkies, temp))
        ShowTime1.append(TempSt)

    data = zip(Dates, ShowTime1)
    data2 = zip(Dates, ShowTime1)
    return render(request, "movie/movie_booking.html", {"data": data, "data2": data2, "movie":movie})

def Create_Sheets(request):
    for i in range(1,89):
        Seats.objects.create(sn = i)
    return redirect("MyMovie:home")





########################################## ADMIN panel############################################

def Admin_Add_Category(request):
    error=False
    if request.method == "POST":
        cat = request.POST["cat"].capitalize().strip()
        data=Movie_Category.objects.filter(name=cat).first()
        if not data:
            Movie_Category.objects.create(name=cat)
            return redirect("MyMovie:movie_home")
        error=True
    return render(request, "movie/add_category.html",{"error":error})

def Admin_Add_Movie(request):
    form = Add_Movie_form()
    if request.method == "POST":
        form = Add_Movie_form(request.POST ,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("MyMovie:add_starcast")
    return render(request, "movie/add_movie.html", {"form":form})

def Admin_Add_Starcast(request):
    form = Add_Starcast_form()
    if request.method == "POST":
        form = Add_Starcast_form(request.POST ,request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("MyMovie:movieList")
    return render(request, "movie/add_movie.html", {"form":form})

def Admin_Add_ShowTime(request):
    talk  = Talkies.objects.all()
    movies = MovieDetails.objects.all()
    if request.method == "POST":
        d = request.POST
        tk = d["talkies"]
        mv = d["movie"]
        dt = d["date"]
        tm = d["time"]
        rs = d["rs"]
        talkies = Talkies.objects.filter(id = tk).first()
        movie = MovieDetails.objects.filter(id = mv).first()
        St = ShowTime.objects.create(talkies=talkies, movie=movie, time=tm,
                                     Rs= rs, date=dt)
        for i in range(1,89):
            Seats.objects.create(talkies=talkies, st=St, sn = i)
        return redirect("MyMovie:movie_home")

    d = {
        "talk":talk, "movies":movies
    }
    return render(request, "movie/add_st.html", d)

def Seat_Booking(request, st_id):
    st = ShowTime.objects.filter(id=st_id).first()
    sheets = Seats.objects.filter(st=st)
    if not request.user.is_authenticated:
        return redirect("MyMovie:login_account")

    if request.method == "POST":
        data = request.POST
        St = data.getlist("cb")
        usr = request.user
        St1 = Seats.objects.filter(usr=usr, status="Pending")
        for i in St1:
            i.status = "Blank"
            i.save()

        for i in St:
            st = Seats.objects.filter(id=i).first()
            st.usr = request.user
            st.status = "Pending"
            st.save()

        return redirect("MyMovie:payment")
    d={
        "s1":sheets[:22],
        "s2":sheets[22:44],
        "s3":sheets[44:66],
        "s4":sheets[66:],
        "st":st
    }

    return render(request, "movie/seat_booking.html", d)

def MakePayment(request):
    usr = request.user
    St = Seats.objects.filter(usr=usr, status="Pending")
    Rs = 0
    for i in St:
        Rs = Rs + i.st.Rs
    payload = {
        'purpose': 'Movie Booking',
        'amount': str(Rs),
        'buyer_name': request.user.username,
        'email': request.user.email,
        'phone': request.user.userdetails_set.first().number,
        'redirect_url': 'http://127.0.0.1:8000/PayCheck/{}/'.format(request.user.username),
        'send_email': 'True',
        'send_sms': 'True',
        'allow_repeated_payments': 'False',
    }
    response = requests.post("https://www.instamojo.com/api/1.1/payment-requests/", data=payload, headers=headers)
    obj = json.loads(response.text)
    print(obj)
    Url= obj["payment_request"]["longurl"]
    Idd = obj["payment_request"]["id"]
    Di = Payment_Id.objects.filter(Usr = usr)
    Di.delete()
    Payment_Id.objects.create(Usr=usr, PayId=Idd)
    return redirect(Url)


    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


from django.http import HttpResponse
def PayChack(request, Usr):
    usr = User.objects.filter(username = Usr).first()
    Di = Payment_Id.objects.filter(Usr=usr).first()
    response = requests.get("https://www.instamojo.com/api/1.1/payment-requests/{}/".format(Di.PayId),headers=headers)
    obj = json.loads(response.text)
    Status = obj["payment_request"]["payments"][0]["status"]
    if Status == "Failed":
        # get request
        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.post(reqUrl, req_params)

        # get response
        response = sendPostRequest(URL, 'CJHXDJIW9NCHNTDVTQHQ1AR41LS8UADT', 'GPUJ4WD5QOPQLJSW', 'stage', request.user.userdetails_set.first().number,
                                   'HRSHIT', 'Booking failed')
        """
          Note:-
            you must provide apikey, secretkey, usetype, mobile, senderid and message values
            and then requst to api
        """
        # print response if you want
        print(response.text)
        return HttpResponse("<h1>Payment Failed</h1>")
    else:
        return HttpResponse("<h1>Payment Done... @@</h1>")

        def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
            req_params = {
                'apikey': apiKey,
                'secret': secretKey,
                'usetype': useType,
                'phone': phoneNo,
                'message': textMessage,
                'senderid': senderId
            }
            return requests.post(reqUrl, req_params)

            # get response

        response = sendPostRequest(URL, 'CJHXDJIW9NCHNTDVTQHQ1AR41LS8UADT', 'GPUJ4WD5QOPQLJSW', 'stage',
                                   request.user.userdetails_set.first().number,
                                   'HRSHIT', 'Booking successfull')
        """
          Note:-
            you must provide apikey, secretkey, usetype, mobile, senderid and message values
            and then requst to api
        """
        # print response if you want
        print(response.text)




