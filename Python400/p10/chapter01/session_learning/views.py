from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def test_session(request):
    name = request.session.get('name')
    if name:
        request.session.flush()
        return HttpResponse(f'Welcome {name}, refresh please.')
    else:
        request.session['name'] = 'Wen'
        return HttpResponse(f'How are you? refresh please.')
