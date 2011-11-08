from .defaults import *

DEBUG = False
TEMPLATE_DEBUG = False
PRODUCTION = True

try:
    from armstrong_website.settings.private import *
except ImportError:
    import sys
    sys.stderr.write("Unable to load armstrong_website.settings.private\n")
    sys.stderr.write("Please see the README for more information.")
    sys.exit(1)
