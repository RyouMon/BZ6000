from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template import loader
# Create your views here.


def index(request):
    print('view func index.')
    return HttpResponse('view function index.')


def test_process_template_response(request):
    print('view func test_process_template_response.')
    template = loader.get_template('middleware_learning/test_process_template_response.html')
    return TemplateResponse(request, template)


def raise_exception(request):
    print('view func raise_exception.')
    # raise an exception
    1 / 0
