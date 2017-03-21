from django.conf.urls import patterns, include, url
from django.contrib import admin
from calc import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^suma/(.*)$', views.sumador, name="suma"),
    url(r'^resta/(.*)$', views.restador, name="resta"),
    url(r'^multi/(.*)$', views.multiplicador, name="multiplicador"),
    url(r'^division/(.*)$', views.divisor, name="divisor"),
)
