from django.urls import path
from Movie.views import *

app_name="MyMovie"
urlpatterns=[

    path("apit", apit, name="apit"),

    ################## admin panel ############


    path('apidd/<int:m_id>/', details, name="details"),

]
