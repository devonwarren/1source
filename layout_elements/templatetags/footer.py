from django import template
from django.template.loader import get_template
from django.template import Context
from journal.models import JournalEntry
from sections.models import Section, SubSection

register = template.Library()

@register.simple_tag
def footer():
	journal = JournalEntry.objects.all().order_by('-published_date')[:3]

	subsections = []
	sections = Section.objects.prefetch_related('subsection_set').all()
	for s in sections:
		subsections.append(s.subsection_set.all())
	section_list = zip(sections, subsections)

	t = get_template('footer.html')
	return t.render(Context({ 'journal' : journal, 'section_list' : section_list }))

