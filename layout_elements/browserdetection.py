import re
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
 
 
class BrowserDetectionMiddleware(object):
    """
    middleware to detect if the user is on an old browser
    """
 
    def process_request(self, request):
        is_old = False
 
        if 'HTTP_USER_AGENT' in request.META:
            user_agent = request.META['HTTP_USER_AGENT']
 
            pattern = "msie [1-8]\."
            prog = re.compile(pattern, re.IGNORECASE)
            match = prog.search(user_agent)
 
            if match:
                is_old = True
 
        if is_old == True:
            t = get_template('unsupported_browser.html')
            html = t.render(Context())
            return HttpResponse(html)