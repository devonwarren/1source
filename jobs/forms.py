from django import forms
from datetime import datetime
from django.forms.widgets import Input, FileInput, NumberInput, \
    Select, CheckboxSelectMultiple, CheckboxInput, RadioSelect
from .models import Application, ApplicationDisability, Job


class PhoneInput(Input):
    input_type = 'tel'


class EmailInput(Input):
    input_type = 'email'


class MoneyInput(NumberInput):
    input_type = 'number'


class ApplicationForm1(forms.Form):
    first_name = forms.CharField(
        max_length=120,
        widget=Input(attrs={'id': 'id_first_name'}))

    middle_initial = forms.CharField(
        widget=Input(attrs={'id': 'id_middle_inital'}),
        max_length=1,
        required=False)

    last_name = forms.CharField(
        max_length=120,
        widget=Input(attrs={'id': 'id_last_name'}))

    phone = forms.CharField(
        widget=PhoneInput(attrs={'id': 'id_phone'}))

    email = forms.CharField(
        max_length=120,
        widget=EmailInput(attrs={'id': 'id_email'}))

    resume = forms.FileField(
        widget=FileInput(attrs={
            'accept':
                '.doc,.docx,application/msword,' +
                'application/vnd.openxmlformats-officedocument' +
                '.wordprocessingml.document',
            'id': 'id_resume'}))

    desired_salary = forms.IntegerField(
        widget=MoneyInput(attrs={
            'min': 10000,
            'step': 2000
        }))

    us_citizenship = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_us_citizenship'}),
        choices=Application.CITIZENSHIP_STATUSES)

    clearance = forms.BooleanField(
        widget=CheckboxInput(attrs={'id': 'id_clearance'}),
        required=False)

    clearance_type = forms.CharField(
        widget=Input(attrs={
            'id': 'id_clearance_type',
            'placeholder': 'example: NACLC, Public Trust, Top Secret'}),
        required=False)


class ApplicationForm2(forms.Form):
    # Allow blank choices
    GENDERS = (('', '----'),) + Application.GENDERS
    RACES = (('', '----'),) + Application.RACES
    REFERRED_OPTIONS = (('', '----'),) + Application.REFERRED_OPTIONS

    gender = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_gender'}),
        choices=GENDERS)

    race = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_race'}),
        choices=RACES)

    race_other = forms.CharField(
        widget=Input(attrs={'id': 'id_race_other'}),
        max_length=120, required=False)

    referred = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_referred'}),
        choices=REFERRED_OPTIONS)

    referred_other = forms.CharField(
        widget=Input(attrs={'id': 'id_referred_other'}),
        max_length=120, required=False)

    veteran = forms.BooleanField(
        widget=CheckboxInput(attrs={'id': 'id_veteran'}),
        required=False)

    military_service = forms.MultipleChoiceField(
        widget=CheckboxSelectMultiple(attrs={'id': 'id_military_service'}),
        choices=Application.MILITARY_OPTIONS, required=False)


class ApplicationForm3(forms.Form):
    DISABILITY_OPTIONS = ApplicationDisability.DISABILITY_OPTIONS

    disability = forms.ChoiceField(
        widget=RadioSelect(attrs={'id': 'id_disability'}),
        choices=DISABILITY_OPTIONS)


class ApplicationReportForm(forms.Form):
    # create an array of years to go through
    application_years_options = [('All', 'All')]

    # Application field changes break the migration functionality without this
    try:
        first_application = Application.objects.all().order_by('-submitted')[0]
        for y in range(first_application.submitted.year, datetime.now().year+1):
            application_years_options.append((y, y),)
    except Exception:
        pass

    job = forms.ModelChoiceField(
        queryset=Job.objects.all(), required=False, empty_label='All')

    year = forms.ChoiceField(choices=application_years_options)
