from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from journal.models import JournalEntry


def journal(request):
	entries = JournalEntry.objects.all().order_by('-published_date')[:5]

	t = get_template('journal.html')
	html = t.render(Context({ 'journal' : entries }))
	return HttpResponse(html)