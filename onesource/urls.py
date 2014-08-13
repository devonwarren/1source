from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from onesource.views import style_guide

urlpatterns = patterns('',
	url(r'^$', style_guide, name='style_guide'),

    url(r'^admin/', include(admin.site.urls)),
)
