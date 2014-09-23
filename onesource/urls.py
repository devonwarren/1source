from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from onesource.views import homepage, style_guide
from journal.views import journal, entry_view
from contact.views import contact
from sections.views import learn_more_view, leadership
from pages.views import page

urlpatterns = patterns('',
	url(r'^$', homepage, name='homepage'),
	url(r'^journal$', journal, name='journal'),
	url(r'^journal/(?P<entry>.+?)/$', entry_view),
	url(r'^contact$', contact, name='contact'),
	url(r'^leadership$', leadership),
	url(r'^learn-more/(?P<subsection>.+?)/$', learn_more_view),
	url(r'^page/(?P<page_alias>.+?)/$', page),
	url(r'^style_guide$', style_guide, name='style_guide'),

	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
