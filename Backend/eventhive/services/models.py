from django.db import models

# Create your models here.

class ServiceCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(null=True, blank=True)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    # availability = models.BooleanField(default=True)  # You may want to change this later
    contact_phone = models.CharField(max_length=15)
    capacity = models.PositiveIntegerField()
    facilities = models.JSONField(blank=True, null=True)
    event_type_compatibility = models.JSONField(blank=True, null=True)
    photos = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='venues', on_delete=models.CASCADE)
    
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
    
    def __str__(self):
        return self.catering_name
    

class PhotographyVideography(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price_weekday = models.DecimalField(max_digits=10, decimal_places=2)
    price_weekend = models.DecimalField(max_digits=10, decimal_places=2)
    contact = models.CharField(max_length=15)
    service_duration = models.DecimalField(max_digits=5, decimal_places=2)  # Duration in hours
    photos = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(ServiceCategory, related_name='photography_videographies', on_delete=models.CASCADE)
    
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
    
    def __str__(self):
        return self.name
    

class EventPlanner(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    available_locations = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    event_type = models.CharField(max_length=100) # Event types they can handle
    contact = models.CharField(max_length=15)
    category = models.ForeignKey(ServiceCategory, related_name='event_planners', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Sports(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(blank=True, null=True)
    price_by_seating = models.JSONField() # JSON with seating types and prices
    event_date = models.DateField()
    seating_map_url = models.URLField(blank=True, null=True)
    ticket_type = models.JSONField()  # Different types of tickets (VIP, Regular, etc.)
    available_tickets_for_each_type = models.JSONField()  # Number of available tickets per type
    category = models.ForeignKey(ServiceCategory, related_name='sports', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class ConcertAndShow(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)
    location_map = models.URLField(blank=True, null=True)
    ticket_type = models.JSONField()
    price_by_ticket = models.JSONField() # JSON with ticket types and prices
    available_tickets_for_each_type = models.JSONField()  # Number of available tickets per type
    performer_name = models.CharField(max_length=200)
    event_date = models.DateField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)  # Duration in hours
    category = models.ForeignKey(ServiceCategory, related_name='concert_and_shows', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=100)    
    location_map = models.URLField(blank=True, null=True)
    room_type = models.JSONField()  # Types of rooms (AC, Non-AC, Suite, etc.)
    price_by_room_type = models.JSONField()  # Prices for each room type
    available_rooms_for_each_type = models.JSONField()  # Available rooms per type
    category = models.ForeignKey(ServiceCategory, related_name='hotels', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class EventType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name