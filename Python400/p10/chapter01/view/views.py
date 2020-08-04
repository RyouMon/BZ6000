from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
# Create your views here.


class MyView(View):
    def get(self, request):
        return HttpResponse('Response by class-based view.')


def test_render(request):
    return render(request, 'view/test_render.html')


def test_redirect(request):
    return redirect(reverse('test_render'), permanent=True)
