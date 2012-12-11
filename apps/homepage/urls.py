from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'apps.homepage.views.index'),
)
