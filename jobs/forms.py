from django import forms
from django.forms.widgets import Input, FileInput, NumberInput, \
    Select, SelectMultiple, CheckboxInput
from .models import Application, MilitaryService


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
        choices=Application.citizenship_statuses)

    clearance = forms.BooleanField(
        widget=CheckboxInput(attrs={'id': 'id_clearance'}),
        required=False)

    clearance_type = forms.CharField(
        widget=Input(attrs={
            'id': 'id_clearance_type',
            'placeholder': 'example: NACLC, Public Trust, Secret'}),
        required=False)


class ApplicationForm2(forms.Form):
    # Allow blank choices
    genders = (('', '----'),) + Application.genders
    races = (('', '----'),) + Application.races
    referred_options = (('', '----'),) + Application.referred_options
    referred_options = (('', '----'),) + Application.referred_options

    gender = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_gender'}),
        choices=genders,
        required=False)

    race = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_race'}),
        choices=races, required=False)

    race_other = forms.CharField(
        widget=Input(attrs={'id': 'id_race_other'}),
        max_length=120, required=False)

    referred = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_referred'}),
        choices=referred_options, required=False)

    referred_other = forms.CharField(
        widget=Input(attrs={'id': 'id_referred_other'}),
        max_length=120, required=False)

    military_service = forms.ModelMultipleChoiceField(
        widget=SelectMultiple(attrs={'id': 'id_military_service'}),
        queryset=MilitaryService.objects.all(), required=False)


class ApplicationForm3(forms.Form):
    disability_options = (('', '----'),) + Application.disability_options

    disability = forms.ChoiceField(
        widget=Select(attrs={'id': 'id_disability'}),
        choices=disability_options)
