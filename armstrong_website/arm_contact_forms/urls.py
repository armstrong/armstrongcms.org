from contact_form.views import contact_form
from django.conf.urls.defaults import patterns, url
# TODO: change to CBV
from django.views.generic.simple import direct_to_template
from .forms import ArmstrongContactForm

# Redefine the URL routes from django-contact-form so we can inject our own form
urlpatterns = patterns('',
    url(r'^$', contact_form,
        {"form_class": ArmstrongContactForm},
        name='contact_form'),
    url(r'^sent/$', direct_to_template,
        {'template': 'contact_form/contact_form_sent.html'},
        name='contact_form_sent'),
)
