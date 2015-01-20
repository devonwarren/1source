import os
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib.formtools.wizard.views import SessionWizardView
from .models import Job, Application, ApplicationDisability, ApplicationLog
from .forms import ApplicationForm1, ApplicationForm2, ApplicationForm3, \
    ApplicationReportForm
import json
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
            veteran=application_data['veteran'],
            military_service=application_data['military_service'],
        )
        app.save()
        app_dis = ApplicationDisability(
            job=job,
            application=app,
            disability=application_data['disability'],
        )
        app_dis.save()

        # save a log of everything
        application_data['resume'] = application_data['resume'].name
        log = ApplicationLog(
            application=app,
            ip_address=self.request.META.get('REMOTE_ADDR'),
            form_data=json.dumps(application_data)
        )
        log.save()

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
    if request.method == 'POST':
        form = ApplicationReportForm(request.POST)
        if form.is_valid():
            return generate_job_application_spreadsheet(form.cleaned_data)
    else:
        form = ApplicationReportForm()
    return render(request, 'job_applications_report.html', {
        'form': form,
        'title': 'Job Applications Report'
    })


def job_application_details(form, worksheet):
    # get job and applicants list
    job = Job.objects.get(id=form['job'].id)
    applicants = Application.objects.filter(job=job)
    if form['year'] and form['year'] != 'All':
        applicants.filter(submitted__year=int(form['year']))

    # add headings
    worksheet.write('A1', 'Application Date')
    worksheet.write('B1', 'Last Name')
    worksheet.write('C1', 'First Name')
    worksheet.write('D1', 'Req # and Position Title')
    worksheet.write('E1', 'Full Time/Part Time')
    worksheet.write('F1', 'Location')
    worksheet.write('G1', 'Race')
    worksheet.write('H1', 'Gender')
    worksheet.write('I1', 'Disposition Code')
    worksheet.write('J1', 'Referral Source')
    worksheet.write('K1', 'Hire Date')
    row = 2

    # Add all the applicants
    for app in applicants:
        # get the applicants

        # Add their info to spreadsheet
        worksheet.write('A' + str(row), app.submitted.strftime('%m/%d/%Y'))
        worksheet.write('B' + str(row), app.last_name)
        worksheet.write('C' + str(row), app.first_name)
        worksheet.write('D' + str(row), job.code + ' ' + job.title)
        if job.fulltime:
            worksheet.write('E' + str(row), 'FT')
        else:
            worksheet.write('E' + str(row), 'PT')
        worksheet.write('F' + str(row), job.location)
        worksheet.write('G' + str(row), app.race)
        worksheet.write('H' + str(row), app.gender)
        worksheet.write('I' + str(row), '')
        worksheet.write(
            'J' + str(row),
            [k for k in Application.REFERRED_OPTIONS if k[0] == app.referred][0][1])
        if app.hired_date:
            worksheet.write(
                'K' + str(row),
                app.hired_date.strftime('%m/%d/%Y'))

        row += 1


def job_application_overview(form, worksheet):
    jobs = Job.objects.all()

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
    row = 2

    # Add all the jobs
    for job in jobs:
        # get the applicants
        if form['year'] == 'All':
            applicants = Application.objects.filter(job=job.id)
        else:
            applicants = Application.objects.filter(
                job=job.id,
                submitted__year=form['year'])
        disabilities = ApplicationDisability.objects.filter(
            application__in=applicants)

        # Add their info to spreadsheet
        worksheet.write('A' + str(row), job.code)
        worksheet.write('B' + str(row), job.title)
        if (job.fulltime):
            worksheet.write('C' + str(row), 'Full Time')
        else:
            worksheet.write('C' + str(row), 'Part Time')
        worksheet.write('D' + str(row), job.location)
        worksheet.write(
            'E' + str(row),
            [k for k in Job.JOB_GROUPS if k[0] == job.group][0][1])

        worksheet.write('F' + str(row), len(applicants))
        worksheet.write('G' + str(row), len(applicants.exclude(race=6)))
        worksheet.write('H' + str(row), len(applicants.filter(gender='F')))
        worksheet.write('I' + str(row), len(applicants.filter(veteran=True)))
        worksheet.write('J' + str(row), len(disabilities.filter(
            disability='Y')))

        # grab the hired applicant if there is one
        hired_app = Application.objects.filter(
            job=job,
            status='H'
            ).order_by('hired_date')
        if hired_app:
            disabled = ApplicationDisability.objects.filter(
                application=hired_app)
            worksheet.write('L' + str(row), hired_app[0].last_name)
            worksheet.write('M' + str(row), hired_app[0].first_name)
            worksheet.write('N' + str(row), hired_app[0].race)
            worksheet.write('O' + str(row), hired_app[0].gender)

            if hired_app[0].veteran:
                worksheet.write('P' + str(row), 'Y')
            else:
                worksheet.write('P' + str(row), 'N')

            if disabled[0].disability == 'Y':
                worksheet.write('Q' + str(row), 'Y')
            else:
                worksheet.write('Q' + str(row), 'N')

            worksheet.write(
                'R' + str(row),
                hired_app[0].submitted.strftime('%m/%d/%Y'))
            worksheet.write(
                'S' + str(row),
                hired_app[0].hired_date.strftime('%m/%d/%Y'))

        row += 1


def generate_job_application_spreadsheet(form_data):
    # create a tmp file to save in
    tmpfile = tempfile.NamedTemporaryFile(prefix="xls")
    workbook = xlsxwriter.Workbook(tmpfile.name)
    # do all the spreadsheet work
    worksheet = workbook.add_worksheet()

    if form_data['job']:
        job_application_details(form_data, worksheet)
    else:
        job_application_overview(form_data, worksheet)

    # done working
    workbook.close()
    output = open(tmpfile.name, 'rb').read()
    # save response so we can close and delete the temp file
    response = HttpResponse(output,
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response[
        'Content-Disposition'] = "attachment; filename=job_applications.xlsx"
    tmpfile.close()
    return response
