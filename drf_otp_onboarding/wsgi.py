"""
WSGI config for drf_otp_onboarding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

#from decouple import config
from django.core.wsgi import get_wsgi_application

# environment = config('ENVIRONMENT')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings."+environment)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_otp_onboarding.settings")

application = get_wsgi_application()
