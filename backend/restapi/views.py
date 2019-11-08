import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
from django.conf import settings
from backend.common.views import *
from backend.models import *


@csrf_exempt
def sample(request):
    return JsonResponse({'result': 200})


@csrf_exempt
def login(request):
    return JsonResponse({'result': 200})


# curl -XPOST http://127.0.0.1:8000/api/v1/regist -H 'Content-Type: application/json' -d '{"user_id":"hello", "user_pw":"world"}'
@csrf_exempt
def regist(request):
    # Parameter Received Basic Structure
    body = bodyParser(request.body)
    if body == None:
        return JsonResponse({'code': 500, 'msg': 'Parameter is invalid'})
    else:
        user_id = body['user_id']
        user_pw = body['user_pw']
        log('user_id', user_id)
        log('user_pw', user_pw)

    # Prevent duplicate membership
    user = TblUser.objects.filter(user_id = user_id)
    if len(user) == 0:
        user = TblUser(
            user_id = user_id,
            user_pw = user_pw,
            regist_date = datetime.datetime.now(),
            update_date = None,
            delete_date = None,
            delete_yn = 'N',
        )
        user.save()
        return JsonResponse({'code': 200, 'msg': 'Your membership has been completed'})
    else:
        return JsonResponse({'code': 400, 'msg': 'This is a user who is already'})
