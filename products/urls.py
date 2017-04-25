from django.conf.urls import url
from django.contrib import admin

from .views import show_all, detail

urlpatterns = [
    url(r'^all$', show_all, name='show_all'),
    url(r'^detail/(?P<product>\d+)/$', detail),
]