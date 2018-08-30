from django.conf.urls import include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from touristsapp import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^locations/$', views.LocationList.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)$', views.LocationDetail.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/visit/$', views.VisitListPost.as_view()),
    url(r'^locations/(?P<pk>[0-9]+)/ratio/$', views.RatioList.as_view()),
    url(r'^visits/$', views.VisitList.as_view()),
    url(r'^visits/(?P<pk>[0-9]+)$', views.VisitDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/ratio/$', views.UserRatioList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]
