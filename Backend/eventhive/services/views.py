from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import Venue, Catering, PhotographyVideography, Entertainment, EventPlanner, Sports, ConcertAndShow, Hotel
from .serializers import VenueSerializer, CateringSerializer, PhotographyVideographySerializer, EntertainmentSerializer, EventPlannerSerializer, SportsSerializer, ConcertShowSerializer, HotelSerializer

# Create your views here.


# Venue Add View
class VenueCreateView(CreateAPIView):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

# Catering Add View
class CateringCreateView(CreateAPIView):
    queryset = Catering.objects.all()
    serializer_class = CateringSerializer

# Photography Add View
class PhotographyCreateView(CreateAPIView):
    queryset = PhotographyVideography.objects.all()
    serializer_class = PhotographyVideographySerializer

# Entertainment Add View
class EntertainmentCreateView(CreateAPIView):
    queryset = Entertainment.objects.all()
    serializer_class = EntertainmentSerializer

# Event Planner Add View
class EventPlannerCreateView(CreateAPIView):
    queryset = EventPlanner.objects.all()
    serializer_class = EventPlannerSerializer

# Sports Add View
class SportsCreateView(CreateAPIView):
    queryset = Sports.objects.all()
    serializer_class = SportsSerializer

# Concert And Show Add View
class ConcertAndShowCreateView(CreateAPIView):
    queryset = ConcertAndShow.objects.all()
    serializer_class = ConcertShowSerializer

# Hotel Add View
class HotelCreateView(CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer