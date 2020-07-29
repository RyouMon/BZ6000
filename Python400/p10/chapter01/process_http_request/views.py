from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    return HttpResponse('hello world!')


def special_case_2003(request, **kwargs):
    msg = kwargs.pop('msg', None)
    return HttpResponse(f'2003, msg from func path(): {msg}')


def year_archive(request, year):
    return HttpResponse(f'archive year {year}.')


def mouth_archive(request, year, mouth):
    return HttpResponse(f'archive year {year}, archive mouth {mouth}.')


def article_detail(request, year, mouth, slug):
    return HttpResponse(f'archive year {year}, archive mouth {mouth}, article {slug}.')


def page(request, num=1):
    return HttpResponse(f'blog page {num}')


def redirect_to_year(request, year):
    return HttpResponseRedirect(reverse('new-year-archive', args=(year,)))
