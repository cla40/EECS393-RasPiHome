from django.conf.urls import patterns, url

from piServer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
