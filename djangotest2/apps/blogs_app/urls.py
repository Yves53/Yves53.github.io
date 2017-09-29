from django.conf.urls import url
from . import views  # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs/$', views.index),  # This line has changed!
    url(r'^blogs/new/$', views.new), # This line has changed!
    url(r'^blogs/create/$', views.create), # This line has changed!
    url(r'^blogs/(?P<number>\d+)/$', views.number), # This line has changed!
    url(r'^blogs/(?P<number>\d+)/edit/$', views.edit), # This line has changed!
    url(r'^blogs/(?P<number>\d+)/delete/$', views.destroy), # This line has changed!
]
