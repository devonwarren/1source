from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = '4k6k60$$&nf4^ugs%^ek@#74p$)guo7qnosr%&2bk@y0t(jmd6'

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += \
    ("debug_toolbar.middleware.DebugToolbarMiddleware", )
