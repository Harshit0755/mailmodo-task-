from django.contrib.auth.models import User
from django.db import models

class Movie_Category(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class MovieDetails(models.Model):
    cat=models.ForeignKey(Movie_Category,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    root = models.CharField(max_length=500, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=2000, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    trailer = models.CharField(max_length=10000, null=True, blank=True)
    producer = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title

class StarCast(models.Model):
    movie=models.ForeignKey(MovieDetails,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    photo = models.ImageField(null=True, blank=True)
    role_as = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class OurCrew(models.Model):
    movie = models.ForeignKey(MovieDetails, on_delete=models.CASCADE, null=True, blank=True)
    type=models.CharField(max_length=50,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class BehindScreen(models.Model):
    movie = models.ForeignKey(MovieDetails, on_delete=models.CASCADE, null=True, blank=True)
    img=models.ImageField(null=True,blank=True)

class Movie_users(models.Model):
    usr=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

class Talkies(models.Model):
    name=models.CharField(max_length=100, null=True,blank=True)
    address=models.CharField(max_length=100, null=True,blank=True)

    def __str__(self):
        return self.name

class ShowTime(models.Model):
    talkies=models.ForeignKey(Talkies, on_delete=models.CASCADE, null=True,blank=True)
    movie=models.ForeignKey(MovieDetails, on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    Rs = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.talkies)

class Seats(models.Model):
    usr = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    talkies = models.ForeignKey(Talkies, on_delete=models.CASCADE, null=True, blank=True)
    st = models.ForeignKey(ShowTime, on_delete=models.CASCADE, null=True, blank=True)
    sn = models.CharField(max_length=10, null=True, blank=True)             #seatno.
    status = models.CharField(max_length=100, default="Blank")

class Payment_Id(models.Model):
    Usr = models.ForeignKey(User, on_delete=models.CASCADE)
    PayId = models.CharField(max_length=120, null=True, blank=True)

class UserDetails(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=10,null=True, blank=True)

    def __str__(self):
        return self.name