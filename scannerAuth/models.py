from django.db import models


class StudentQrAuth(models.Model):
    qr_id = models.AutoField(db_column='QR_id', primary_key=True)  # Field name made lowercase.
    s_name = models.TextField(db_column='S_Name', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    s_enrollment_no = models.BigIntegerField(db_column='S_Enrollment_No', blank=True, null=True)  # Field name made lowercase.
    s_email = models.CharField(db_column='S_email', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    is_qr_scanned = models.BooleanField(db_column='Is_QR_scanned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Student_QR_Auth'
