from settings.defaults import *

DEBUG = False
TEMPLATE_DEBUG = False
PRODUCTION = True

try:
    import local_settings
except ImportError:
    pass
