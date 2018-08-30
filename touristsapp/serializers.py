from rest_framework import serializers
from touristsapp.models import Location, Visit
from django.contrib.auth.models import User


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Visit
        fields = ('id', 'user', 'date', 'ratio', 'location_id')


class LocationSerializer(serializers.ModelSerializer):
    locations = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description', 'locations')


class UserSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_fields = ['visits']


class VisitUserRatioSerializer(serializers.ModelSerializer):
    visitors = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_fields = ['visits']


class VisitRatioSerializer(serializers.ModelSerializer):
    visitors = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description', 'visitors')


class UserDetailSerializer(serializers.ModelSerializer):
    visits = VisitSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'visits')
