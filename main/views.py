from django.shortcuts import render, HttpResponse
from django.template import loader


def index(request):
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

