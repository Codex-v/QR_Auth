from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home",scan),
    path('ScanQR/<int:id>',scannedQR),
    path('genQR',createQR)
]
