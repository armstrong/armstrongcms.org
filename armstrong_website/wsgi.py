import os, sys

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir))
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__))))

from django.core.handlers.wsgi import WSGIHandler

if not "DJANGO_SETTINGS_MODULE" in os.environ:
	os.environ["DJANGO_SETTINGS_MODULE"] = "armstrong_website.settings.production"

application = WSGIHandler()
