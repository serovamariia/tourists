from rest_framework import serializers
from touristsapp.models import Location, Visit


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description')


class VisitSerializer(serializers.Serializer):
    class Meta:
        model = Visit
        fields = ('id', 'user_id', 'location_id', 'date', 'ratio')
