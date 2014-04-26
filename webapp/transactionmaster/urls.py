from	django.conf.urls	import	patterns,	include,	url
from	django.contrib	import	admin
from	usermaster.views	import	UserLoginView
from	usermaster.views	import	UserCreationView
from	usermaster.views	import	UserUpdateView
from	usermaster.views	import	UserDeleteView

admin.autodiscover()

urlpatterns	=	patterns('',

	url(r'^userlogin/$',	'usermaster.views.UserLoginView'),
	url(r'^createuser/$',	UserCreationView.as_view()),
	url(r'^updateuser/(?P<pk>\d+)/$',	UserUpdateView.as_view()),
	url(r'^deleteuser/(?P<pk>\d+)/$',	UserDeleteView.as_view()),

)

