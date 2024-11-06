from django.urls import path, include
from .views import *

urlpatterns = [
    path('venue/', VenueCreateView.as_view(), name='add_venue'),
    path('catering/', CateringCreateView.as_view(), name='add_catering'),
    path('photography/', PhotographyCreateView.as_view(), name='add_photography'),
    path('entertainment/', EntertainmentCreateView.as_view(), name='add_entertainment'),
    path('event-planner/', EventPlannerCreateView.as_view(), name='add_event_planner'),
    path('sports/', SportsCreateView.as_view(), name='add_sports'),
    path('concert-and-show/', ConcertAndShowCreateView.as_view(), name='add_concert_show'),
    path('hotel/', HotelCreateView.as_view(), name='add_hotel'),
]