from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_to_list/(?P<number>\d+)$', views.add_to_list),
    url(r'^remove_from_list/(?P<number>\d+)$', views.remove_from_list),
    url(r'^user_quotes/(?P<number>\d+)$', views.user_quotes),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^dashboard/$', views.dashboard),
    url(r'^dashboard/add_quote/$', views.add_quote),
]
