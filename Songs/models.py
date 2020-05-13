from django.db import models

class Album(models.Model):
    name=models.CharField(max_length=50)
    artists=models.CharField(max_length=50)
    image=models.CharField(max_length=5000)
    date=models.DateField(auto_now_add=True)
    company=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=50)
    artists=models.ForeignKey(Album,on_delete=models.CASCADE,null=True,blank=True)
    duration=models.CharField(max_length=50)
    poster=models.CharField(max_length=50,null=True)
    audio=models.CharField(max_length=500,null=True)
    video=models.CharField(max_length=500,null=True)
    def __str__(self):
        return self.title
