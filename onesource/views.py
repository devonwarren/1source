from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def style_guide(request):
    t = get_template('style_guide.html')
    html = t.render(Context())
    return HttpResponse(html)
    
def homepage(request):
    t = get_template('homepage.html')
    html = t.render(Context())
    return HttpResponse(html)
    