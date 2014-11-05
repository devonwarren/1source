from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from .models import Job


def job_listings(request):
	jobs = Job.objects.filter(active=True).order_by('title')

	t = get_template('job_listings.html')
	html = t.render(Context({ 'jobs' : jobs }))
	return HttpResponse(html)

def job_details(request, job_id):
	job = get_object_or_404(Job, id=job_id)
	
	t = get_template('job_details.html')
	html = t.render(Context({ 
		'job' : job,
	}))
	return HttpResponse(html)