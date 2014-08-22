from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from onesource.views import homepage, style_guide

urlpatterns = patterns('',
	url(r'^$', homepage, name='homepage'),
	url(r'^style_guide$', style_guide, name='style_guide'),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^ckeditor/', include('ckeditor.urls')),
)
