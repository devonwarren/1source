from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from onesource.views import homepage, unsupported_browser
from journal.views import journal, entry_view
from news.views import news_list, news_view
from contact.views import contact, contact_thanks
from sections.views import learn_more_view, leadership
from jobs.views import job_listings, job_details
from pages.views import page

urlpatterns = patterns('',
	url(r'^$', homepage, name='homepage'),
	url(r'^journal/$', journal, name='journal'),
	url(r'^journal/(?P<entry>.+?)/$', entry_view),
	url(r'^news/$', news_list, name='news_list'),
	url(r'^news/(?P<entry>.+?)/$', news_view),
	url(r'^contact/$', contact, name='contact'),
	url(r'^contact/thanks/$', contact_thanks, name='contact_thanks'),
	url(r'^leadership/$', leadership),
	url(r'^learn-more/(?P<subsection>.+?)/$', learn_more_view),
	url(r'^jobs/$', job_listings),
	url(r'^job/(?P<job_id>.+?)/$', job_details),
	url(r'^page/(?P<page_alias>.+?)/$', page),
	url(r'^unsupported_browser/$', unsupported_browser),


	url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'onesource.views.page_not_found'
