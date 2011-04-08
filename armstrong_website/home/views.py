from django.shortcuts import render_to_response
from django.template import RequestContext

from armstrong.core.arm_wells.models import Well

def index(request, template_name='home/index.html'):
    context = {}
    wells = Well.objects.filter(type__slug='generic')
    context['well'] = wells[0] if wells else None 
    return render_to_response(template_name, context, 
                              context_instance=RequestContext(request))