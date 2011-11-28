from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from armstrong import hatband as admin
admin.autodiscover()

from armstrong.core.arm_wells.views import SimpleWellView

urlpatterns = patterns('',
    url(r'^contact/', include('arm_contact_forms.urls')),
    url(r'^$', SimpleWellView.as_view(template_name='home/index.html',
                                      well_title='Generic'), name='home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)