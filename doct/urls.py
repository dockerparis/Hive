from django.conf.urls import patterns, include, url
from django.contrib import admin
from doct.app import views
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^$', 'doct.app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^task/$', views.new_task, name='new_task'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.show_task, name='show_task'),
    url(r'^task/update/(?P<pk>[0-9]+)/$', views.update_task, name='update_task'),
    url(r'^task/new/$', views.new_task, name='new_task'),
    url(r'^list/$', RedirectView.as_view(url='/list/1', permanent=False), name='index'),
    url(r'^list/(?P<pk>[0-9]+)$', views.list_task, name='list_task'),
    url(r'^contribute/(?P<pk>[0-9]+)/$', views.contribute_task, name='contribute_task'),
)
