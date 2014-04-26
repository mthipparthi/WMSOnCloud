from django.conf.urls import patterns
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

from usermaster.views import UserLoginView
from usermaster.views import UserCreationView
from usermaster.views import UserUpdateView
from usermaster.views import UserDeleteView
from usermaster.views import UserDetailView

urlpatterns    =    patterns('',

    url(r'^userlogin/$',    'usermaster.views.UserLoginView',name='user_login',),
    url(r'^createuser/$',    UserCreationView.as_view(),name='user_create',),
    url(r'^updateuser/(?P<pk>\d+)/$',    UserUpdateView.as_view(),name='user_update',),
    url(r'^deleteuser/(?P<pk>\d+)/$',    UserDeleteView.as_view(),name='user_delete',),
    url(r'^searchusers/$',    'usermaster.views.UserSearchView',name='user_search',),
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail',),
)

