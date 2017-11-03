from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    template_name = 'polls/index.html'
    return render(request, template_name)
