from django import template
from django.template.loader import get_template
from django.template import Context
from journal.models import JournalEntry

register = template.Library()

@register.simple_tag
def footer():
	journal = JournalEntry.objects.all().order_by('-published_date')[:5]
	t = get_template('footer.html')
	return t.render(Context({ 'journal' : journal }))

