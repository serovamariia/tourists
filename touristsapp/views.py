from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from touristsapp.models import Location, Visit
from touristsapp.serializers import (LocationSerializer, UserSerializer,
                                     VisitRatioSerializer, VisitSerializer,
                                     VisitUserRatioSerializer)


class CreateUserView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class VisitListPost(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            location_id=self.kwargs.get('pk'),
        )


class RatioList(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = VisitRatioSerializer


class VisitList(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserRatioList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = VisitUserRatioSerializer
