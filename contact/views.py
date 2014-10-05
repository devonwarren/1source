from django.shortcuts import render
from contact.forms import ContactForm
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                'Contact Us from "' + cd['name'],
                cd['message'],
                cd.get('email', 'devon.warren+from@gmail.com'),
                ['devon.warren@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_thanks(request):
    t = get_template('contact_thanks.html')
    html = t.render(Context({}))
    return HttpResponse(html)