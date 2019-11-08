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
        print('{key} : '.format(key=key) + val)
