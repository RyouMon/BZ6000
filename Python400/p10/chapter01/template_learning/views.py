from django.shortcuts import render

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