from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import storemaster.urls
import usermaster.urls
import item.urls

urlpatterns    =    patterns('',
    url(r'^$',    TemplateView.as_view(template_name='index.html')),
    url(r'^apphome/',TemplateView.as_view(template_name='app.html')),
    url(r'^css/',    include(admin.site.urls)),
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^storemaster/',    include(storemaster.urls)),
    url(r'^usermaster/',    include(usermaster.urls)),
    url(r'^item/',    include(item.urls)),
)
# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
