import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def per_site_cache(request):
    time = datetime.datetime.now()
    return HttpResponse(f'这个页面已经被缓存，有效期100秒，上次的缓存时间：{time}')


def view(request):
    time = datetime.datetime.now()
    return HttpResponse(f'这个页面没有进行缓存，访问时间：{time}')


def cached_view(request):
    time = datetime.datetime.now()
    return HttpResponse(f'这个页面已经被缓存，有效期60秒，上次的缓存时间：{time}')


def cached_template(request):
    time = datetime.datetime.now()
    return render(request, 'cache_learning/test_template_fragment_caching.html', {'time': time})
