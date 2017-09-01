"""
WSGI config for orbital1417 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
#import sys
'''
path = '/home/HuhY/orbital1417/Orbital1417'

if path not in sys.path:
    sys.path.append(path)

os.environ [ 'DJANGO_SETTINGS_MODULE']="website.settings"

from django.core.wsgi import get_wsgi_application
application= get_wsgi_application()
'''


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orbital1417.settings")

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application= DjangoWhiteNoise(application)
