from django.shortcuts import render, get_list_or_404
from .models import Student
from datetime import datetime
# Create your views here.


def template_variables(request):
    context = {
        'nums': [1, 2, 3],
        'person': {
            'name': 'Kana',
            'age': 19,
        },
        'request': request
    }
    return render(request, 'template_learning/template_variables.html', context=context)


def student_list(request):
    context = {
        'students': get_list_or_404(Student),
        'boys': [],
    }
    return render(request, 'template_learning/for_and_if_tags.html', context)


def filters(request):
    context = {
        'num': 10,
        'word': 'hello world!',
        'date': datetime.strptime('2013-12-02 12:34:13', '%Y-%m-%d %H:%M:%S'),
    }
    return render(request, 'template_learning/filters.html', context)
