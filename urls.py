from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('^$', 'url.views.create'),
    ('^(?P<sha_hash>[a-z\d]{1,40})/$', 'url.views.access'),
)
