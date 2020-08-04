from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponse
from .models import Student
# Create your views here.


class MyView(View):
    def get(self, request):
        return HttpResponse('Response by class-based view.')


def test_render(request):
    return render(request, 'view/test_render.html')


def test_redirect(request):
    return redirect(reverse('test_render'), permanent=True)


def student_detail(request, name):
    student = get_object_or_404(Student, name=name)
    context = {
        'student': student,
    }
    return render(request, 'view/student.html', context=context)
