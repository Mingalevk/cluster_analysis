__author__ = 'user'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<object_id>\d+)/$', views.detail, name='detail'),
]