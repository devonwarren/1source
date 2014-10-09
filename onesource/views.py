from django.template.loader import get_template
from django.template import RequestContext, Context
from django.http import HttpResponse
from sections.models import Section, SubSection, HeroImage


def page_not_found(request):
    return render(request,'404.html')
    
def homepage(request):
	subsections = []
	sections = Section.objects.prefetch_related('subsection_set').all()
	for s in sections:
		subsections.append(s.subsection_set.all())
	section_list = zip(sections, subsections)

	hero_images = HeroImage.objects.all().order_by('?')
	
	t = get_template('homepage.html')
	html = t.render(RequestContext(request, {
		'section_list' : section_list, 
		'heroes' : hero_images,
	}))
	return HttpResponse(html)
