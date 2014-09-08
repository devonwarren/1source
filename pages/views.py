from django.shortcuts import get_object_or_404
from pages.models import Page
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def page(request, page_alias):
	page = get_object_or_404(Page, alias=page_alias)

	t = get_template('page.html')
	html = t.render(Context({ 'page' : page }))
	return HttpResponse(html)
