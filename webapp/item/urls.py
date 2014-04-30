from django.conf.urls import patterns, include, url

from item import views

urlpatterns = patterns('',
    url(r'^$', views.ListItemMater.as_view(), name='item-list',),
    url(r'^add/$', views.CreateItemMater.as_view(), name='item-new',),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateItemMaster.as_view(), name='item-edit',),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteItemMaster.as_view(), name='item-remove',),
    url(r'^(?P<pk>\d+)/$', views.ItemMasterView.as_view(), name='item-view',),
    url(r'^search/$', views.ItemSearchView),
    url(r'^assignLocnSearch/$', views.AssignLocationSearch),
)