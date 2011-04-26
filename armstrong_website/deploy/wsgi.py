import os, sys

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))

from django.core.handlers.wsgi import WSGIHandler
os.environ["DJANGO_SETTINGS_MODULE"] = "armstrong_website.production_settings"
application = WSGIHandler()
