from django.db import models
from django.utils import timezone

# Create your models here.

class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    FACILITY_CHOICES = [
        ('wifi', 'WiFi'),
        ('ac', 'A/C'),
        ('parking', 'Parking'),
        ('restrooms', 'Restrooms'),
        ('audio_visual', 'Audio-Visual Equipment'),
        ('stage_lighting', 'Stage and Lighting'),
        ('lounge_area', 'Lounge Area'),
    ]

    EVENT_COMPATIBILITY_CHOICES = [
        ('conference', 'Conference'),
        ('trade_show', 'Trade Show'),
        ('party', 'Party'),
        ('wedding', 'Wedding'),
        ('festival', 'Festival'),
        ('exhibition', 'Exhibition'),
    ]
    venue_name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(null=True, blank=True)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    contact_phone = models.CharField(max_length=15)
    capacity = models.PositiveIntegerField()
    facilities = models.JSONField(choices=FACILITY_CHOICES, blank=True, null=True)
    event_type_compatibility = models.JSONField(choices=EVENT_COMPATIBILITY_CHOICES, blank=True, null=True)
    photos = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='venues', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.venue_name
    

class Catering(models.Model):
    catering_name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)
    cuisine_type = models.CharField(max_length=100, null=True, blank=True)
    minimum_order_size = models.PositiveIntegerField()
    photos = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='caterings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.catering_name
    

class PhotographyVideography(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)
    photos = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='photography_videographies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Entertainment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)
    performance_duration = models.DecimalField(max_digits=5, decimal_places=2)  # Duration in hours
    category = models.ForeignKey(ServiceCategory, related_name='entertainments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class EventPlanner(models.Model):
    EVENT_CHOICES = [
        ('conference', 'Conference'),
        ('trade_show', 'Trade Show'),
        ('party', 'Party'),
        ('wedding', 'Wedding'),
        ('festival', 'Festival'),
        ('exhibition', 'Exhibition'),
        ('charity_event', 'Charity Event'),
        ('workshop', 'Workshop'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event_type = models.CharField(max_length=100, choices=EVENT_CHOICES, blank=True,null=True)
    contact = models.CharField(max_length=15)
    category = models.ForeignKey(ServiceCategory, related_name='event_planners', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Sports(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(blank=True, null=True)
    event_date = models.DateField()
    seating_map_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='sports', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class SportsTicketType(models.Model):
    sport = models.ForeignKey('Sports', related_name='ticket_types', on_delete=models.CASCADE)
    seating_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} - {self.price}"


class ConcertAndShow(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(blank=True, null=True)
    performer_name = models.CharField(max_length=200)
    event_date = models.DateField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)  # Duration in hours
    category = models.ForeignKey(ServiceCategory, related_name='concert_and_shows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ConcertTicketType(models.Model):
    concert = models.ForeignKey('ConcertAndShow', related_name='ticket_types', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} - {self.price}"


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='hotels', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)  # e.g., Suite, Standard, etc.
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.room_type} - {self.price}"


class Facility(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name