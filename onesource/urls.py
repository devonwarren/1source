from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from onesource.views import homepage, style_guide
from journal.views import journal

urlpatterns = patterns('',
	url(r'^$', homepage, name='homepage'),
	url(r'^journal$', journal, name='journal'),
	url(r'^style_guide$', style_guide, name='style_guide'),

	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
