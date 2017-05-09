from django.shortcuts import *
import logging
logger = logging.getLogger('sourceDns.webdns.views')


def logs(request):
    try:
        logger.info(1111111111111111)
    except Exception,e:
            logger.error(22222222222222222)
    return render(request, 'index.html')
