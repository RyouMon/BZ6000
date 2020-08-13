from logging import getLogger
from django.http import HttpResponse
# Create your views here.


logger = getLogger(__name__)


def log(request):
    logger.debug('TEST DEBUG MESSAGE.')
    logger.info('TEST INFO MESSAGE.')
    return HttpResponse('Test Logging.')
