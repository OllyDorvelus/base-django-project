"""
# WSGI config for base project.
#
# It exposes the WSGI callable as a module-level variable named ``application``.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
# """

import os

from configurations.wsgi import get_wsgi_application

# APPNAME.SETTINGS
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

application = get_wsgi_application()