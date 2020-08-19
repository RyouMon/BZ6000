import datetime
from django.http import HttpResponse


# Create your views here.
def per_site_cache(request):
    time = datetime.datetime.now()
    return HttpResponse(f'这个页面已经被缓存，有效期100秒，上次的缓存时间：{time}')
