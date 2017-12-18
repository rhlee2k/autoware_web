from django.conf.urls import url

from . import views

app_name = 'autoware_web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.index, name='mypage'),
    url(r'^$', views.index, name='login'),
    url(r'^$', views.index, name='logout'),
    url(r'^docker/$', views.docker_install, name='docker'),
]
