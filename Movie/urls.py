from django.urls import path
from Movie.views import *

app_name="MyMovie"
urlpatterns=[
    path('', Movie_Home, name="movie_home"),
    path('contact/', Movie_Contact, name="movie_contact"),
    path('movie_list/', MovieList, name="movieList"),
    path('movie_details/<int:m_id>/', Movie_Details, name="movieDetails"),
    path('movie_booking/<int:m_id>/', Movie_Booking, name="movieBooking"),
    path('seat_booking/<int:st_id>/', Seat_Booking, name="seatBooking"),
    path("create_sheets/", Create_Sheets, name = "sheets"),
    path('accounts/login/', Login, name = "login"),
    path('logout/', Logout, name = "logout"),
    path("payMentMake", MakePayment, name = "payment"),
    path('register/', Register, name = "register"),
    path("add_show_time/", Admin_Add_ShowTime, name = "add_show_time"),
    path("PayCheck/<str:Usr>/", PayChack, name="paycheck"),

    ################## admin panel ############

    path('admin_add_category/', Admin_Add_Category, name="add_category"),
    path('admin_add_movie/', Admin_Add_Movie, name="add_movie"),
    path('admin_add_starcast/', Admin_Add_Starcast, name="add_starcast"),

]
