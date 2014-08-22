from django.template.loader import get_template
from django.template import RequestContext, Context
from django.http import HttpResponse
from sections.models import Section, SubSection


def style_guide(request):
	t = get_template('style_guide.html')
	html = t.render(Context())
	return HttpResponse(html)
    
def homepage(request):
	sections = Section.objects.all()
	subsections = SubSection.objects.all()
	
	t = get_template('homepage.html')
	html = t.render(RequestContext(request, {
		'sections':sections, 
		'subsections':subsections, 
	}))
	return HttpResponse(html)
