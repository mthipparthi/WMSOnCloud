from	django.conf.urls	import	patterns,	include,	url
from	django.contrib	import	admin
from	storemaster.views	import	index
from	storemaster.views	import	StoreMasterCreate
from	storemaster.views	import	StoreMasterUpdate
from	storemaster.views	import	StoreMasterDelete
from	storemaster.views	import	StoreMasterDetailView
admin.autodiscover()

urlpatterns	=	patterns('',
	#	Examples:
	#	url(r'^$',	'store.views.home',	name='home'),
	#	url(r'^blog/',	include('blog.urls')),
		#url(r'^$',	index),
	#url(r'^storemaster/',	index),
	#url(r'storemaster/add/$',	StoreMasterCreate.as_view(),	name='storemaster_add'),
	url(r'^add/$',	StoreMasterCreate.as_view()),
	url(r'^update/(?P<pk>\d+)/$',	StoreMasterUpdate.as_view()),
	url(r'^delete/(?P<pk>\d+)/$',	StoreMasterDelete.as_view()),
	url(r'^(?P<pk>\d+)/$',	StoreMasterDetailView.as_view(),	name='storemaster-detail'),
)

