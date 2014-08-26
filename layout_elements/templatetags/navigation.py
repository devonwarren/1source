from django import template
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

register = template.Library()

@register.simple_tag
def navigation(active = ''):
	t = get_template('navigation.html')
	return t.render(Context({ 'active' : active }))

