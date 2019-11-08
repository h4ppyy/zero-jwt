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
