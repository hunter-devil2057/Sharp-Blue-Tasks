from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import json, requests
import finnhub

finnhub_client = finnhub.Client(api_key=settings.FINNHUB_CLIENT_APIKEY)

# Create your views here.
def home(request):
    try:
        # Fetch the live quote and symbol lookups
        quote = finnhub_client.quote("AAPL")
        symbols = finnhub_client.symbol_lookup("apple")

        # Combine both datasets into a single 'api' object
        api = {"quote": quote, "symbols": symbols}
    except Exception as e:
        api = "Error ....."
    return render(request, 'home.html', {"api": api})
    # return HttpResponse("<h1>Hello, </h1>")

def about(request):
    return render(request, 'about.html', {})