from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse

from masters.models import Adult



def index(request):
    latest_adults_list = Adult.objects.order_by('first_name')[:5]
    
    template = loader.get_template('index.html')
    context = {
        'latest_adults_list': latest_adults_list,
    }
    return HttpResponse(template.render(context, request))    