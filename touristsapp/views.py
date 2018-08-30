from touristsapp.models import Location, Visit
from touristsapp.serializers import LocationSerializer, VisitSerializer, VisitRatioSerializer, VisitUserRatioSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from touristsapp.serializers import UserSerializer, UserDetailSerializer
from rest_framework import permissions
from touristsapp.permissions import IsOwnerOrReadOnly
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import View
from django.contrib import auth


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'locations': reverse('location-list', request=request, format=format),
        'visits': reverse('visit-list', request=request, format=format)
    })


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRatio(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitUserRatioSerializer


class RatioList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = VisitRatioSerializer


class VisitList(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
