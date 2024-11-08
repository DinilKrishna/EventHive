from django.db import models
from datetime import timedelta
from django.utils import timezone
from account.models import CustomUser
from services.models import *

# Create your models here.

class VenueAvailability(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE) 

    @property
    def total_dates(self):
        # Generate a list of dates from tomorrow for the next 30 days
        start_date = timezone.now().date() + timedelta(days=1)
        return [(start_date + timedelta(days=i)) for i in range(30)]
    
    @property
    def available_dates(self):
        # Get all booked dates for this venue
        booked_dates = VenueBooking.objects.filter(venue=self.venue).values_list('booked_date', flat=True)
        # Subtract booked dates from total dates
        return [date for date in self.total_dates if date not in booked_dates]
    

class VenueBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(max_length=15, blank=True, null=True)
    booked_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Booking for {self.venue} by {self.user}"
    

# Catering Availability (One slot per day, available or not)
class CateringAvailability(models.Model):
    catering_service = models.ForeignKey(Catering, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)  # True if available, False if booked

    def update_availability(self, is_booked=True):
        """Set availability to False if booked or True if available."""
        self.is_available = not is_booked
        self.save()

    def __str__(self):
        return f"{self.catering_service} on {self.date} - {'Available' if self.is_available else 'Booked'}"
    
    
class CateringBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    catering = models.ForeignKey(Catering, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(max_length=15, blank=True, null=True)
    event_date = models.DateField()
    guest_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Catering Booking by {self.user} for {self.catering} on {self.event_date}"
    

# Photography/Videography Availability (One session per day)
class PhotographyAvailability(models.Model):
    photography_service = models.ForeignKey(PhotographyVideography, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)  # True if available, False if booked

    def update_availability(self, is_booked=True):
        """Set availability to False if booked or True if available."""
        self.is_available = not is_booked
        self.save()

    def __str__(self):
        return f"{self.photography_service} on {self.date} - {'Available' if self.is_available else 'Booked'}"
    

class PhotographyVideographyBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    photography_service = models.ForeignKey(PhotographyVideography, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(max_length=15, blank=True, null=True)
    event_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Photography Booking by {self.user} for {self.photography_service} on {self.event_date}"
    

# Entertainment Availability (One performance slot per day)
class EntertainmentAvailability(models.Model):
    entertainment_service = models.ForeignKey(Entertainment, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)  # True if available, False if booked

    def update_availability(self, is_booked=True):
        """Set availability to False if booked or True if available."""
        self.is_available = not is_booked
        self.save()

    def __str__(self):
        return f"{self.entertainment_service} on {self.date} - {'Available' if self.is_available else 'Booked'}"
    

class EntertainmentBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    entertainment = models.ForeignKey(Entertainment, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(max_length=15, blank=True, null=True)
    event_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Entertainment Booking by {self.user} for {self.entertainment} on {self.event_date}"
    

# Event Planner Availability (One event per day)
class EventPlannerAvailability(models.Model):
    event_planner = models.ForeignKey(EventPlanner, on_delete=models.CASCADE)
    date = models.DateField()
    is_available = models.BooleanField(default=True)  # True if available, False if booked

    def update_availability(self, is_booked=True):
        """Set availability to False if booked or True if available."""
        self.is_available = not is_booked
        self.save()

    def __str__(self):
        return f"{self.event_planner} on {self.date} - {'Available' if self.is_available else 'Booked'}"
    

class EventPlannerBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event_planner = models.ForeignKey(EventPlanner, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(max_length=15, blank=True, null=True)
    event_date = models.DateField()
    event_type = models.CharField(max_length=100, choices=EventPlanner.EVENT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Event Planner Booking by {self.user} for {self.event_planner} on {self.event_date}"
    

# Sports Ticket Availability (Does not require dates, only tracks ticket type availability)
class SportsTicketAvailability(models.Model):
    sports_event = models.ForeignKey(Sports, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(SportsTicketType, on_delete=models.CASCADE)
    tickets_remaining = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sports_event} ({self.ticket_type}) - {self.tickets_remaining} tickets remaining"
    

class SportsBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sports_event = models.ForeignKey(Sports, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(SportsTicketType, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    event_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sports Booking by {self.user} for {self.sports_event} on {self.event_date}"
    

# Concert Ticket Availability (Does not require dates, only tracks ticket type availability)
class ConcertTicketAvailability(models.Model):
    concert = models.ForeignKey(ConcertAndShow, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(ConcertTicketType, on_delete=models.CASCADE)
    tickets_remaining = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.concert} ({self.ticket_type}) - {self.tickets_remaining} tickets remaining"
    

class ConcertBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    concert = models.ForeignKey(ConcertAndShow, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey(ConcertTicketType, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    quantity = models.PositiveIntegerField()
    event_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Concert Booking by {self.user} for {self.concert} on {self.event_date}"
    

# Hotel Room Availability (Tracks room type availability by date)
class RoomAvailability(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    date = models.DateField()
    rooms_available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.hotel} ({self.room_type}) on {self.date} - {self.rooms_available} rooms available"

    def update_availability(self, rooms_booked):
        """Decrease availability by the number of rooms booked."""
        if rooms_booked <= self.rooms_available:
            self.rooms_available -= rooms_booked
            self.save()
        else:
            raise ValueError("Not enough rooms available")


class HotelBooking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    no_of_rooms = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hotel Booking by {self.user} for {self.hotel} from {self.check_in_date} to {self.check_out_date}"