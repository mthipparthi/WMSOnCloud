from django.conf.urls import patterns, include, url

from storemaster import views

urlpatterns = patterns('',

    url(r'^add/$', views.CreateStoreMaster.as_view(), name='store-new',),
    url(r'^(?P<pk>\d+)/$', views.StoreDetailView.as_view(), name='store-view',),
)