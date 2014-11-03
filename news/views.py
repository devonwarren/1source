from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import Announcement


def news_list(request):
	entries = Announcement.objects.all().order_by('-published_date')[:5]

	t = get_template('news.html')
	html = t.render(Context({ 'news' : entries }))
	return HttpResponse(html)

def news_view(request, entry):
	entry = get_object_or_404(Announcement, slug=entry)
	entry.content = entry.body
	
	t = get_template('page.html')
	html = t.render(Context({ 
		'page' : entry,
	}))
	return HttpResponse(html)