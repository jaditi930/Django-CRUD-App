from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('create/',views.createFlights),
    path('show/<int:flight_id>/',views.show),
    path('delete/',views.deleteFlights),
    path('show/<int:flight_id>/update/<int:flightid>/',views.updateFlight,name="updateFlight"),
]