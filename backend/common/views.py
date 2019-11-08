import json
from django.conf import settings


def bodyParser(body):
    try:
        body = json.loads(body)
    except BaseException:
        body = None
    return body


def log(key, val):
    if settings.DEBUG_LOG == True:
        try:
            print('{key} : '.format(key=key), val)
        except BaseException:
            print(val)


def sizeof_fmt(num, suffix='b'):
    for unit in ['', 'k', 'm', 'g', 't', 'p', 'e', 'z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)
