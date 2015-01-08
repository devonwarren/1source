import os
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.formtools.wizard.views import SessionWizardView
from .models import Job, Application, ApplicationDisability
from .forms import ApplicationForm1, ApplicationForm2, ApplicationForm3
import xlsxwriter
import tempfile


class ApplicationWizard(SessionWizardView):
    file_storage = FileSystemStorage(
        location=os.path.join(settings.MEDIA_ROOT, 'applications'))
    form_list = [ApplicationForm1, ApplicationForm2]

    # forms and templates for the job applications
    FORMS = [("0", ApplicationForm1),
             ("1", ApplicationForm2),
             ("2", ApplicationForm3)]

    TEMPLATES = {"0": "job_apply1.html",
                 "1": "job_apply2.html",
                 "2": "job_apply3.html"}

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        application_data = {}
        for form in form_list:
            application_data = dict(list(application_data.items()) +
                                    list(form.cleaned_data.items()))

        job = Job.objects.get(id=kwargs['job_id'])
        app = Application(
            job=job,
            first_name=application_data['first_name'],
            last_name=application_data['last_name'],
            middle_initial=application_data['middle_initial'],
            phone=application_data['phone'],
            email=application_data['email'],
            resume=application_data['resume'],
            desired_salary=application_data['desired_salary'],
            gender=application_data['gender'],
            us_citizenship=application_data['us_citizenship'],
            clearance=application_data['clearance'],
            clearance_type=application_data['clearance_type'],
            race=application_data['race'],
            race_other=application_data['race_other'],
            referred=application_data['referred'],
            referred_other=application_data['referred_other'],
            military_service=application_data['military_service'],
        )
        app.save()
        app_dis = ApplicationDisability(
            job=job,
            application=app,
            disability=application_data['disability'],
        )
        app_dis.save()

        t = get_template('job_apply_thanks.html')
        context = Context({'job': job})
        html = t.render(context)
        return HttpResponse(html)


def job_listings(request):
    jobs = Job.objects.filter(active=True).order_by('title')

    t = get_template('job_listings.html')
    html = t.render(Context({
        'jobs': jobs,
    }))
    return HttpResponse(html)


def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    t = get_template('job_details.html')
    html = t.render(Context({
        'job': job,
    }))
    return HttpResponse(html)


def job_apply(request, job_id):
    if request.method == 'POST':
        form = ApplicationWizard(request.POST, request.FILES)
    else:
        form = ApplicationWizard()

    return form.as_view(ApplicationWizard.FORMS)


def job_application_spreadsheet(request):
    # create a tmp file to save in
    tmpfile = tempfile.NamedTemporaryFile(prefix="xls")
    workbook = xlsxwriter.Workbook(tmpfile.name)
    # do all the spreadsheet work
    worksheet = workbook.add_worksheet()
    # add headings
    worksheet.write('A1', 'Job ID')
    worksheet.write('B1', 'Position Name')
    worksheet.write('C1', 'Full Time/Part Time')
    worksheet.write('D1', 'Location')
    worksheet.write('E1', 'EEO-1 Category/Job Group')
    worksheet.write('F1', 'Total Applicants')
    worksheet.write('G1', 'Minorities')
    worksheet.write('H1', 'Female')
    worksheet.write('I1', 'Veteran')
    worksheet.write('J1', 'Disability')
    worksheet.write('L1', 'Last Name')
    worksheet.write('M1', 'First Name')
    worksheet.write('N1', 'Race')
    worksheet.write('O1', 'Gender')
    worksheet.write('P1', 'Veteran')
    worksheet.write('Q1', 'Disability')
    worksheet.write('R1', 'Date of Application')
    worksheet.write('S1', 'Date of Hire')
    # done working
    workbook.close()
    output = open(tmpfile.name, 'rb').read()
    # save response so we can close and delete the temp file
    response = HttpResponse(output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=job_applications.xlsx"
    tmpfile.close()
    return response
