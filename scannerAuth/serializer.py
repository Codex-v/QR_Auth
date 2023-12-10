from rest_framework import serializers
from .models import *

class StudentQRAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentQrAuth
        fields = ['s_name','s_enrollment_no','s_email','is_qr_scanned']

class StudentQrAuthGenrateQRSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = StudentQrAuth
        fields = ['s_name','s_enrollment_no']

