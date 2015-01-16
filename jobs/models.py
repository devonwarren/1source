from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from datetime import datetime


class Job(models.Model):
    JOB_GROUPS = (
        ('E', 'Executive'),
        ('P', 'Professional'),
        ('1', '1st Level Manager'),
        ('T', 'Technician'),
        ('A', 'Administrative'),
    )

    active = models.BooleanField(
        default=False, help_text='Enable this if the job should be listed')
    fulltime = models.BooleanField(
        default=True, help_text='Enable if this is a full-time position')
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=15)
    location = models.CharField(max_length=250, blank=True)
    security_clearance = models.CharField(max_length=250, blank=True)
    duties = RichTextField()
    qualifications = RichTextField()
    desired = RichTextField(blank=True)
    group = models.CharField(
        max_length=1, choices=JOB_GROUPS, help_text='EEO-1 Category')
    closed_date = models.DateTimeField(blank=True, null=True)
    closed_reason = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' (' + self.code + ')'

    def get_absolute_url(self):
        return '/job/' + str(self.id) + '/'

    def save(self, *args, **kw):
        # if closing the job update the closed date
        if not self.active:
            if self.pk is not None:
                orig = Job.objects.get(pk=self.pk)
                if orig.active:
                    self.closed_date = datetime.now()
            else:
                self.closed_date = datetime.now()

        super(Job, self).save(*args, **kw)


class Application(models.Model):
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('D', 'I do not wish to answer'),
    )

    CITIZENSHIP_STATUSES = (
        ('Y', 'Yes'),
        ('A', 'No, but I am authorized to work in the US'),
        ('N', 'No, and I am not authorized to work in the US')
    )

    STATUSES = (
        ('N', 'New'),
        ('I', 'Reviewing'),
        ('R', 'Rejected'),
        ('H', 'Hired'),
        ('D', 'Declined'),
    )

    REJECTED_REASONS = (
        ('S', 'Skills'),
        ('E', 'Years of Experience'),
        ('U', 'US Citizenship'),
        ('C', 'Clearance Requirement'),
        ('O', 'Other'),
        ('IS', 'Interviewed - Skills'),
        ('IE', 'Interviewed - Years of Experience'),
        ('IP', 'Interviewed - Presentation/Communication Skills'),
        ('SB', 'Selected but failed badging'),
    )

    RACES = (
            ('1', 'American Indian/Alaskan'),
            ('2', 'Asian'),
            ('3', 'Black/African American'),
            ('4', 'Hispanic/Latino'),
            ('5', 'Hawaiian/Pacific Islander'),
            ('6', 'White/Caucasian'),
            ('7', 'Other'),
            ('8', 'Two or more'),
            ('0', 'I do not wish to answer'),
    )

    REFERRED_OPTIONS = (
        ('W', '1Source Website'),
        ('L', 'LinkedIn'),
        ('M', 'Monster'),
        ('D', 'Dice'),
        ('I', 'Indeed'),
        ('E', 'Employee Referral'),
        ('F', 'Former Employee'),
        ('S', 'State Employment Commission'),
        ('C', 'Contract Transition'),
        ('O', 'Other'),
    )

    MILITARY_OPTIONS = (
        ('P', 'Pre-Vietnam Era'),
        ('V', 'Post-Vietnam Era'),
        ('D', 'Disabled Veteran'),
        ('R', 'Recently Separated Veteran'),
        ('A', 'Active Wartime or Campaign Badge'),
        ('M', 'Armed Forces Service Medal Veteran'),
    )

    job = models.ForeignKey(Job)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    middle_initial = models.CharField(max_length=1, blank=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes')
    desired_salary = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDERS)
    us_citizenship = models.CharField(
        max_length=1, choices=CITIZENSHIP_STATUSES)
    clearance = models.BooleanField(
        default=False, help_text='Do you have a security clearance?')
    clearance_type = models.CharField(
        max_length=120, blank=True,
        help_text='example: NACLC, Public Trust, Secret')
    race = models.CharField(max_length=1, choices=RACES)
    race_other = models.CharField(max_length=120, blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    referred = models.CharField(max_length=1, choices=REFERRED_OPTIONS)
    referred_other = models.CharField(max_length=120, blank=True)
    military_service = MultiSelectField(blank=True, choices=MILITARY_OPTIONS)

    # internal tracking fields
    status = models.CharField(max_length=1, choices=STATUSES, default='N')
    rejected_reason = models.CharField(
        max_length=2, choices=REJECTED_REASONS, blank=True)
    rejected_explaination = models.TextField(blank=True)
    notes = models.TextField(blank=True, help_text='Internal staff notes')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + \
            ' (' + self.job.title + ')'


# Keep disability entries seperate to comply with federal regulations
class ApplicationDisability(models.Model):
    DISABILITY_OPTIONS = (
        ('Y', 'YES, I HAVE A DISABILITY (or previously had a disability)'),
        ('N', 'NO, I DON\'T HAVE A DISABILITY'),
        ('D', 'I DON\'T WISH TO ANSWER'),
    )

    job = models.ForeignKey(Job)
    application = models.ForeignKey(Application)
    disability = models.CharField(
        default='D', max_length=1, choices=DISABILITY_OPTIONS)


class ApplicationLog(models.Model):
    application = models.ForeignKey(Application)
    ip_address = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    form_data = models.TextField(blank=True)
