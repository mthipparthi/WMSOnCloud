from django.conf.urls import patterns, include, url

from inventory import views

urlpatterns = patterns('',
    url(r'^$', views.ListLocationInventory.as_view(), name='locnInventory-list',),
    #url(r'^add$', views.CreateItemMater.as_view(), name='item-new',),
    url(r'^update/(?P<pk>\d+)/$', views.UpdateLocationInventory.as_view(), name='locninventory-edit',),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteLocationInventory.as_view(), name='locninventory-remove',),
    url(r'^assignLocation/$', views.AssignLocation,),
    url(r'^search/$', views.searchLocationInventory),
    #url(r'^(?P<pk>\d+)/$', views.ItemMasterView.as_view(), name='item-view',),
    #url(r'^search/$', views.searchItem),
)