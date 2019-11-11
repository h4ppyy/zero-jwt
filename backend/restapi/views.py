import json
import datetime
import jwt
import uuid
import os
from random import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from backend.common.views import *
from backend.models import *


@csrf_exempt
def sample(request):
    return render(request, 'backend/sample.html')


# curl -XPOST http://127.0.0.1:8000/api/v1/login -H 'Content-Type: application/json' -d '{"user_id":"hello", "user_pw":"world"}'
@csrf_exempt
def login(request):
    # Parameter Received Basic Structure
    body = bodyParser(request.body)
    if body == None:
        return JsonResponse({'code': 500, 'msg': 'Parameter is invalid'})
    else:
        user_id = body['user_id']
        user_pw = body['user_pw']
        log('user_id', user_id)
        log('user_pw', user_pw)

    # Login Logic
    user = TblUser.objects.filter(user_id = user_id)
    if len(user) != 0:
        user = user[0]
        # I didn't put an expiration date in the payload
        # Expiration time needs to be added
        payload = { 'user_id': user.user_id }
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM).decode("utf-8")
        log('token', token)
        return JsonResponse({'code': 200, 'msg': 'Membership login completed', 'token': token})
    else:
        return JsonResponse({'code': 404, 'msg': 'Not a valid member'})


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



# curl -XPOST http://127.0.0.1:8000/api/v1/regist -H 'Content-Type: application/json' -d '{"user_id":"hello", "user_pw":"world"}'
@csrf_exempt
def database(request):
    # Verify the validity of the back-end
    token = request.POST.get('token')
    try:
        jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    except BaseException:
        return JsonResponse({'code': 403, 'msg': 'not auth'})

    # Prevent duplicate membership
    user = TbUserData.objects.filter(dateTime = dateTime)
    if len(user) == 0:
        user = TbUserData(
            dateTime = dateTime,
            timestamp = timestamp,
            accleX = accleX,
            accleY = accleY,
            accleZ = accleZ,
            roll = roll,
            pitch = pitch,
            azimuth = azimuth,
            gyroX = gyroX,
            gyroY = gyroY,
            gyroZ = gyroZ,
            gpsLat = gpsLat,
            gpsLon = gpsLon,
            gpsAlt = gpsAlt,
            gpsAcc = gpsAcc,
            gpsTime = gpsTime,
            NgpsLat = NgpsLat,
            NgpsLon = NgpsLon,
            NgpsAlt = NgpsAlt,
            NgpsAcc = NgpsAcc,
            NgpsTime = NgpsTime,
            regist_date = datetime.datetime.now(),
            update_date = None,
            delete_date = None,
            delete_yn = 'N',
        )
        user.save()
        return JsonResponse({'code': 200, 'msg': 'Your membership has been completed'})
    else:
        return JsonResponse({'code': 400, 'msg': 'This is a user who is already'})

@csrf_exempt
def randomLogin(request):
    users = TblUser.objects.all()
    idx = randint(0, len(users)-1)
    log('idx', idx)
    user = users[idx]
    payload = { 'user_id': user.user_id }
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM).decode("utf-8")
    log('token', token)
    return JsonResponse({
        'code': 200,
        'msg': 'Membership login completed',
        'token': token,
        'user_id': user.user_id
    })


@csrf_exempt
def saveFile(request):
    # Verify the validity of the back-end
    token = request.POST.get('token')
    try:
        jwt.decode(token, settings.JWT_SECRET_KEY, settings.JWT_ALGORITHM)
    except BaseException:
        return JsonResponse({'code': 403, 'msg': 'not auth'})

    # Save file locally
    if 'input_file' in request.FILES:
        file = request.FILES['input_file']
        upload_root = settings.UPLOAD_ROOT
        real_name = file.name
        save_name = str(uuid.uuid4()).replace('-', '')
        ext = file.name.split('.')[-1]
        real_size = file.size
        save_size = sizeof_fmt(file.size)
        save_path = upload_root + save_name

        if not os.path.exists(upload_root):
            os.makedirs(upload_root)

        fs = FileSystemStorage()
        filename = fs.save(save_path, file)

        # Save "save_path" to save the file in the database
        # Fill in the database stored logic here
        # Good luck

        return JsonResponse({'code': 200, 'msg': 'File save completed'})
    else:
        return JsonResponse({'code': 500, 'msg': 'File save failed'})
