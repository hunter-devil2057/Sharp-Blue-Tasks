from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.conf import settings
import requests

# Create your views here.
# def home(response):
#     return HttpResponse("<h1>Hello, World</h1>")


class Home(View):
    template_name = "input.html"     # should always be in string
    def get(self, request):
        # return render(request, 'input.html')
        return render(request, self.template_name)

    def post(self, request):
        ship_num = request.POST.get('shipment_num')
        print(ship_num)

        url = 'https://api.sinay.ai/container-tracking/api/v2/shipment'
        api_key = settings.API_KEY
        parameter = {'shipmentNumber': ship_num}        # value is the user input
        header = {'API_KEY': api_key, 'Accept': 'application/json'}
        
        # for multiple parameters, we should make dictionary in case of APIs.

        response = requests.get(url, params = parameter, headers = header, timeout = 30)     # returns in the form of object
        api_response_data = response.json()
        print(api_response_data)
        return render(request, self.template_name)