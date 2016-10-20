from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^confirmpage/(?P<id>\d+)$', views.confirmpage),
    url(r'^confirm/(?P<id>\d+)$', views.confirm)
]
