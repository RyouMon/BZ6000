from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.


class MyView(View):
    def get(self, request):
        return HttpResponse('Response by class-based view.')
