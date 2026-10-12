from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from shipments.models import *

# Create your views here.
class Home(View):
    def get(self, request):
        metadata = {
            "shipmentType": "BL",
            "shipmentNumber": "SYDG03100300",
            "sealine": "ONEY",
            "sealineName": "Ocean Network Express (ONE)",
            "shippingStatus": "IN_TRANSIT",
            "updatedAt": "2026-10-09T01:19:55Z",
        }
        newMetaData = MetaDataInfo.objects.create(
            shipmentType = metadata["shipmentType"], 
            shipmentNumber=metadata["shipmentNumber"], 
            sealine=metadata["sealine"], 
            sealineName=metadata["sealineName"], 
            shippingStatus=metadata["shippingStatus"], 
            updatedAt=metadata["updatedAt"])
        print(newMetaData)
        print(newMetaData.id)
        print(newMetaData.shipmentType)
        # print(newMetaData.id)
        return HttpResponse("<h1><strong>abc</strong></h1>")