import os
from .defaults import *

DEBUG = False
TEMPLATE_DEBUG = False
PRODUCTION = True


BCC_EMAIL = os.environ["BCC_EMAIL"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
