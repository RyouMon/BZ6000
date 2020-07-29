from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('hello world!')


def special_case_2003(request):
    return HttpResponse('2003')


def year_archive(request, year):
    return HttpResponse(f'archive year {year}.')


def mouth_archive(request, year, mouth):
    return HttpResponse(f'archive year {year}, archive mouth {mouth}.')


def article_detail(request, year, mouth, slug):
    return HttpResponse(f'archive year {year}, archive mouth {mouth}, article {slug}.')


def page(request, num=1):
    return HttpResponse(f'blog page {num}')
