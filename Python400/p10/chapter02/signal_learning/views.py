from django.http import HttpResponse
from . import signals
# Create your views here.


def index(request):
    signals.index_signal.send(sender='view function: index', request=request)
    return HttpResponse('Test Pre Index Request Signal.')
