from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'register/$', views.register, name='register'),
    url(r'profile/$', views.profile, name='profile'),
]

