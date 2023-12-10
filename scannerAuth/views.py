from django.shortcuts import render
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.response import Response
from .models import StudentQrAuth
from rest_framework import status
from .serializer import *
from .utils import Util

@api_view(['GET'])
def scan(request):
    student_objs = StudentQrAuth.objects.filter(is_qr_scanned=0)
    stuSrializer = StudentQRAuthSerializer(student_objs,many=True)
    return Response({"message":"Qr code is not scanned to this peoples",'data':stuSrializer.data})

@api_view(['GET'])
def createQR(request):
    genrateQRSerizlizer = StudentQrAuthGenrateQRSerizlizer(StudentQrAuth.objects.filter(is_qr_scanned=0),many=True)
    for datas in genrateQRSerizlizer.data:
        json = {
            "name":datas['s_name'],
            "rollNo":datas['s_enrollment_no']
            }
        encrypted_data = Util.encrypt_data(json,settings.STATIC_KEY)
        Util.generate_qr_code(encrypted_data,f"{datas['s_name']}.png")
        
    return Response({"message":"create qr is called !"})


@api_view(['POST'])
def scannedQR(request,id):
    if StudentQrAuth.objects.filter(is_qr_scanned=1,s_enrollment_no=id):
        return Response({"User verified":"can't let in this person again"})
    else:
        StudentQrAuth.objects.filter(is_qr_scanned=0,s_enrollment_no=id).update(is_qr_scanned=1)
        return Response({"User verified":"User has been verified and Qr code is scanned"})
    
    