from django.conf.urls import patterns, include, url

from sales import views

urlpatterns = patterns('',
  url(r'^beginSales/$', views.initialiseSales, name='beginsale',),
  url(r'^sellItem/$', views.sellItem, name='sell_item',),
)
