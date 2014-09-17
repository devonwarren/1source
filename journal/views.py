from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from journal.models import JournalEntry


def journal(request):
	entries = JournalEntry.objects.all().order_by('-published_date')[:5]

	t = get_template('journal.html')
	html = t.render(Context({ 'journal' : entries }))
	return HttpResponse(html)

def entry_view(request, entry):
	entry = get_object_or_404(JournalEntry, slug=entry)
	entry.content = entry.body
	
	t = get_template('page.html')
	html = t.render(Context({ 
		'page' : entry, 
		'bgimage' : entry.image_web.url, 
		'active_nav' : 'journal',
	}))
	return HttpResponse(html)