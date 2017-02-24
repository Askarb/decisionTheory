from main import core
from main.models import *
from django.template import loader
from django.shortcuts import render, HttpResponse


def index(request):
    context = {}
    template = loader.get_template('svg-index.html')
    return HttpResponse(template.render(context, request))


def wp(request):
    context = {
        'wp': core.wp()
    }
    template = loader.get_template('main/wp.html')
    return HttpResponse(template.render(context, request))


def emv(request):
    context = {
        'emv': core.emv(),
        'max_emv': core.emv_max()
    }
    template = loader.get_template('main/emv.html')
    return HttpResponse(template.render(context, request))


def report_emv(request):
    context = core.emv_report()
    context['wp'] = core.wp()
    context['probability'] = core.check_propability()
    template = loader.get_template('main/reportEMV.html')
    return HttpResponse(template.render(context, request))


def cp_max(request):
    context = {
        'cp_max': core.cp_max()
    }

    template = loader.get_template('main/cp_max.html')
    return HttpResponse(template.render(context, request))


def col(request):

    context = {
        'col': core.col()
    }
    template = loader.get_template('main/col.html')
    return HttpResponse(template.render(context, request))


def wol(request):

    context = {
        'wol': core.col()
    }
    template = loader.get_template('main/wol.html')
    return HttpResponse(template.render(context, request))


def eol(request):

    context = {
        'eol': core.eol(),
        'min_eol': core.min_eol()
    }
    template = loader.get_template('main/eol.html')
    return HttpResponse(template.render(context, request))


def report_eol(request):
    context = core.eol_report()
    context['wp'] = core.wp()
    context['probability'] = core.check_propability()
    template = loader.get_template('main/reportEOL.html')
    return HttpResponse(template.render(context, request))

