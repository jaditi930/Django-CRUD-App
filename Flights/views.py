from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Flights
# Create your views here.
def home(request):
    flights=Flights.objects.all()
    return render(request,"home.html",{"flights":flights})

def createFlights(request):
    if request.method=="POST":
        start=request.POST["Starting Point"]
        end=request.POST["Destination"]
        new_flight=Flights(start_point=start,dest=end)
        new_flight.save()
    return redirect("/")
def show(request,flight_id):
    flight=Flights.objects.get(id=flight_id)
    return render(request,"show.html",{"flight":flight})
def deleteFlights(request):
    if request.method=="POST":
        flight_id=request.POST["id"]
        del_flight=Flights.objects.get(id=flight_id)
        del_flight.delete()
    return redirect("/")

def updateFlight(request,flight_id,flightid):
    # if request.method=="POST":
    #     id=request.POST["uid"]
    query=request.GET.get('q')
    new_sf=""
    new_d=""
    for p,q in enumerate(query):
        if q!=" ":
            new_sf+=q
        else:
            break
    new_d+=query[p+1:]
    flight=Flights.objects.get(id=flightid)
    flight.start_point=new_sf
    flight.dest=new_d
    flight.save()
    return redirect(f"/show/{flightid}")


    