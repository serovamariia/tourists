from rest_framework import serializers
from touristsapp.models import Location, Visit
from django.contrib.auth.models import User
from django.db.models import Avg


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Visit
        fields = ('id', 'user', 'date', 'ratio', 'user_id')


class LocationSerializer(serializers.ModelSerializer):
    locations = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description', 'locations')


class UserSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'visits')


class VisitRatioSerializer(serializers.ModelSerializer):
    locations = VisitSerializer(many=True, read_only=True)
    count = serializers.ReadOnlyField(source='locations.count')
    avg = serializers.SerializerMethodField()

    def get_avg(self, obj):
        return obj.locations.all().aggregate(Avg('ratio'))['ratio__avg']

    class Meta:
        model = Location
        fields = ('count', 'avg', 'locations')


class VisitUserRatioSerializer(serializers.ModelSerializer):
    visits = VisitSerializer(many=True, read_only=True)
    count = serializers.ReadOnlyField(source='visits.count')
    avg = serializers.SerializerMethodField()

    def get_avg(self, obj):
        return obj.visits.all().aggregate(Avg('ratio'))['ratio__avg']

    class Meta:
        model = User
        fields = ('count', 'avg', 'visits')


class UserDetailSerializer(serializers.ModelSerializer):
    visits = VisitSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'visits')
