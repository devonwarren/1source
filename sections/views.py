from django.shortcuts import get_object_or_404
from sections.models import Section, SubSection, StaffProfile
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def learn_more_view(request, subsection):
	subsec = get_object_or_404(SubSection, slug=subsection)
	subsec.title  = '<a href="/#' + subsec.section.slug + '">' + subsec.section.title + '</a> : ' + subsec.name
	if (subsec.slug == 'technical-competencies'):
		subsec.teaser = """Certified in:<br>
			ISO 9001:2008 Certified<br>
			CMMI Maturity Level III (Software Development)<br>
			Top Secret Facility Clearance
		"""
	subsec.content  = subsec.learn_more

	t = get_template('page.html')
	html = t.render(Context({ 
		'page' : subsec, 
		'bgimage' : subsec.section.image_web.url, 
		'active_nav' : subsec.section.slug,
	}))
	return HttpResponse(html)

def leadership(request):
	founders = StaffProfile.objects.filter(founder=True)
	profiles = StaffProfile.objects.filter(founder=False)
	section = Section.objects.get(slug='story')

	t = get_template('leadership.html')
	html = t.render(Context({ 
		'founders' : founders,
		'profiles' : profiles,
		'section' : section
	}))
	return HttpResponse(html)
