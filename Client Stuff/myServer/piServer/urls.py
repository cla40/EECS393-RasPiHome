from django.conf.urls import patterns, url
from piServer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
