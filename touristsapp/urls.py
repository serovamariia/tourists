from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from rest_framework.routers import DefaultRouter
from touristsapp import views


router = DefaultRouter()
router.register(r'locations', views.LocationViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^register/$', views.CreateUserView.as_view()),
    url(r'^sign_in/', obtain_jwt_token),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/$', views.LocationDetail.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/visit/$', views.VisitListPost.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/ratio/$', views.RatioList.as_view()),
    url(r'^visits/$', views.VisitList.as_view()),
    url(r'^visits/(?P<pk>[0-9]+)/$', views.VisitDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/ratio/$', views.UserRatioList.as_view()),
    path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
