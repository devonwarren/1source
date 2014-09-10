from django.shortcuts import get_object_or_404
from sections.models import SubSection
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def learn_more_view(request, subsection):
	subsec = get_object_or_404(SubSection, slug=subsection)
	subsec.title  = subsec.name
	subsec.content  = subsec.learn_more


	t = get_template('page.html')
	html = t.render(Context({ 'page' : subsec, 'bgimage' : subsec.section.image_web.url }))
	return HttpResponse(html)
