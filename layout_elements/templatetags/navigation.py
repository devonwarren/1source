from django import template
from django.template.loader import get_template
from django.template import Context

register = template.Library()

@register.simple_tag
def navigation(active = '', logoTheme = 'color'):
	t = get_template('navigation.html')
	return t.render(Context({ 'active' : active, 'logoTheme' : logoTheme }))

