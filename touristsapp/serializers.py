from rest_framework import serializers
from touristsapp.models import Location, Visit
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    visits = serializers.PrimaryKeyRelatedField(many=True, queryset=Visit.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'visits')


class LocationSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all(), required=False)

    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description', 'locations')


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    location = serializers.ReadOnlyField(source='locations.name')

    class Meta:
        model = Visit
        fields = ('id', 'user', 'date', 'ratio', 'location')
