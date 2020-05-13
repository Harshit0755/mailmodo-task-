from django.contrib import admin
from django.urls import path, include
from Songs.views import *
from django.conf import settings
from django.conf.urls.static import static
from Movie.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Song_home/', Home, name="home"),
    path('album/<int:ID>', Albums, name="albums"),
    path('songs/<int:ID>', Songs, name="songs"),
    path('add_album/', Add_Album, name="add_album"),
    path('login/', Login, name="Login"),
    path('logout/', Logout, name="Logout"),
    path('register/', Register, name="register"),
    path('add_song<int:Album_Id>/', Add_Song, name="add_song"),



    path('', include('Movie.urls', namespace="MyMovie") ),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
