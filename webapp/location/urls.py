from django.conf.urls import patterns, include, url

from location import views

urlpatterns = patterns('',
    url(r'^$', views.ListLocationMaster.as_view(), name='locn-list',),
    url(r'^add$', views.CreateLocationMaster.as_view(), name='locn-new',),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateLocationMaster.as_view(), name='locn-edit',),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteLocationMaster.as_view(), name='locn-remove',),
    url(r'^(?P<pk>\d+)/$', views.LocationMasterView.as_view(), name='locn-view',),
    #url(r'^search/$', views.searchItem),
)