from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from .models import Job, Application, ApplicationForm


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

def job_apply(request, job_id):
	job = get_object_or_404(Job, id=job_id)

	# go back to details if the job is no longer active
	if not job.active:
		return HttpResponseRedirect(job.get_absolute_url())

	if request.method == 'POST':
		form = ApplicationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			t = get_template('job_apply_thanks.html')
			html = t.render(Context({
				'job' : job
			}))
			return HttpResponse(html)
	else:
		form = ApplicationForm()
	return render(request, 'job_apply.html', { 'form' : form, 'job' : job })