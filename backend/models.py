from django.db import models


class TblUser(models.Model):
    user_id = models.CharField(max_length=255, blank=False, null=False)
    user_pw = models.CharField(max_length=255, blank=False, null=False)
    regist_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'tbl_user'

class TbUserData(models.Model):
    dateTime = models.CharField(max_length=255, blank=False, null=False)
    timestamp = models.CharField(max_length=255, blank=False, null=False)
    accleX = models.CharField(max_length=255, blank=False, null=False)
    accleY = models.CharField(max_length=255, blank=False, null=False)
    accleZ = models.CharField(max_length=255, blank=False, null=False)
    roll = models.CharField(max_length=255, blank=False, null=False)
    pitch = models.CharField(max_length=255, blank=False, null=False)
    azimuth = models.CharField(max_length=255, blank=False, null=False)
    gyroX = models.CharField(max_length=255, blank=False, null=False)
    gyroY = models.CharField(max_length=255, blank=False, null=False)
    gyroZ = models.CharField(max_length=255, blank=False, null=False)
    gpsLat = models.CharField(max_length=255, blank=False, null=False)
    gpsLon = models.CharField(max_length=255, blank=False, null=False)
    gpsAlt = models.CharField(max_length=255, blank=False, null=False)
    gpsAcc = models.CharField(max_length=255, blank=False, null=False)
    gpsTime = models.CharField(max_length=255, blank=False, null=False)
    NgpsLat = models.CharField(max_length=255, blank=False, null=False)
    NgpsLon = models.CharField(max_length=255, blank=False, null=False)
    NgpsAlt = models.CharField(max_length=255, blank=False, null=False)
    NgpsAcc = models.CharField(max_length=255, blank=False, null=False)
    NgpsTime = models.CharField(max_length=255, blank=False, null=False)
    regist_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    delete_date = models.DateTimeField(blank=True, null=True)
    delete_yn = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'tbl_data'
