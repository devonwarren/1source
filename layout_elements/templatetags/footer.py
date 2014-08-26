from django import template
from django.template.loader import get_template
from django.template import Context

register = template.Library()

@register.simple_tag
def footer():
	t = get_template('footer.html')
	return t.render(Context())

