from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers

from touristsapp.models import Location, Visit


class VisitSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    locations = serializers.ReadOnlyField(source='location_id')

    class Meta:
        model = Visit
        fields = ('id', 'user', 'date', 'ratio', 'user_id', 'locations')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'country', 'city', 'name', 'description')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    visits = VisitSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'visits')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class VisitRatioSerializer(serializers.ModelSerializer):
    visitors = VisitSerializer(many=True, read_only=True)
    count = serializers.ReadOnlyField(source='visitors.count')
    avg = serializers.SerializerMethodField()

    def get_avg(self, obj):
        return obj.visitors.all().aggregate(Avg('ratio'))['ratio__avg']

    class Meta:
        model = Location
        fields = ('count', 'avg', 'visitors')


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
