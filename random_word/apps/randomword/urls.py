from django.conf.urls import url
from . import views  # This line is new!
urlpatterns = [
    url(r'^$', views.index),  # This line has changed!
    url(r'^randomword/$', views.index),  # This line has changed!
    url(r'^randomword/reset/$', views.reset),  # This line has changed!
]
