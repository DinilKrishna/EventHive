from rest_framework import serializers
from .models import Venue, Catering, PhotographyVideography, Entertainment, EventPlanner, Sports, ConcertAndShow, Hotel
from services.models import ServiceCategory

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            venue_category = ServiceCategory.objects.get(name="Venues")
            data['category'] = venue_category
        return data

class CateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catering
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            catering_category = ServiceCategory.objects.get(name="Catering")
            data['category'] = catering_category
        return data

class PhotographyVideographySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotographyVideography
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            photo_category = ServiceCategory.objects.get(name="Photography")
            data['category'] = photo_category
        return data

class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainment
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            entertainment_category = ServiceCategory.objects.get(name="Entertainment")
            data['category'] = entertainment_category
        return data

class EventPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPlanner
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            event_planner_category = ServiceCategory.objects.get(name="Event Planners")
            data['category'] = event_planner_category
        return data

class SportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sports
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            sports_category = ServiceCategory.objects.get(name="Sports")
            data['category'] = sports_category
        return data

class ConcertShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcertAndShow
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            concert_category = ServiceCategory.objects.get(name="Concerts and Shows")
            data['category'] = concert_category
        return data

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

    def validate(self, data):
        if not data.get('category'):
            hotel_category = ServiceCategory.objects.get(name="Hotels")
            data['category'] = hotel_category
        return data
