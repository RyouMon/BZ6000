from django.shortcuts import render
from datetime import datetime


def index(request):
    context = {
        'current_time': datetime.now()
    }
    return render(request, 'deployment_learning/index.html', context=context)
