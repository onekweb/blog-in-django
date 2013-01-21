from django.conf.urls.defaults import *
from apps.homepage.feeds import ArchiveFeed

urlpatterns = patterns('apps.homepage.views',
url(r'^$', 'index', name='homepage_index'),
url(r'^about/$','about',  name='homepage_about'),
url(r'^archive/$','archive',  name='homepage_archive'),
url(r'^contact/$','contact',  name='homepage_contact'),
)

urlpatterns += patterns('',
(r'^feed/archive/$', ArchiveFeed()),                        
)
