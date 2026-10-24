from django.db.models import Prefetch
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.conf import settings
from django.utils import timezone as django_timezone
from django.utils.dateparse import parse_datetime
import requests

from api.models import *

# Create your views here.
class HomeView(View):
    template_name = "input.html"
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        ship_num = request.POST.get('shipment_num')
        print(ship_num)
        url = 'https://api.sinay.ai/container-tracking/api/v2/shipment'
        api_key = settings.API_KEY
        parameter = {'shipmentNumber': ship_num}
        header = {'API_KEY': api_key, 'Accept': 'application/json'}
        response = requests.get(url, params = parameter, headers = header, timeout = 30)

        if response.status_code != 200:
            return render(request, self.template_name, {"error": "Shipment not Found...."})
        api_response_data = response.json()
        meta = api_response_data['metadata']
        pol = api_response_data['route']['pol']
        pod = api_response_data['route']['pod'] 
        pol_port, _ = Port.objects.get_or_create(
            locode = pol['location']['locode'], 
            defaults={
                'name': pol['location']['name'],
                'country': pol['location']['country'],
                'countryCode': pol['location']['countryCode'],
            },
        )
        pod_port, _ = Port.objects.get_or_create(
            locode = pod['location']['locode'], 
            defaults={
                'name': pod['location']['name'],
                'country': pod['location']['country'],
                'countryCode': pod['location']['countryCode'],
            },
        )
        shipment, _ = Shipment.objects.update_or_create(
            shipmentNumber=meta['shipmentNumber'],
            defaults={
                'shipmentType': meta['shipmentType'],
                'sealine': meta['sealine'],
                'sealineName': meta['sealineName'],
                'shippingStatus': meta['shippingStatus'],
                'pol': pol_port,
                'pol_date': parse_datetime(pol['date']) if pol['date'] else None,
                'pol_actual': bool(pol['actual']),
                'pod': pod_port,
                'pod_date': parse_datetime(pod['date']) if pod['date'] else None,
                'pod_actual': bool(pod['actual']),
            },
        )
        # Vessels
        shipment.vessels.all().delete()
        for v in api_response_data['vessels']:
            Vessel.objects.create(shipment=shipment, name=v['name'])
        print("Timezone object:", django_timezone)
        # print("Timezone module:", django_timezone.__module__)
        now = django_timezone.now()
        # Containers
        for c in api_response_data['containers']:
            container, _ = Container.objects.update_or_create(
                number = c['number'], 
                defaults = {
                    'shipment': shipment,
                    'isoCode': c['isoCode'],
                    'sizeType': c['sizeType'],
                    'status': c['status'],
                }, 
            )

            # Events: delete old ones and add again (avoids duplicates)
            container.events.all().delete()

            # Save ONLY the events whose date is already in the past
            past_events = []
            for e in c.get('events', []):
                event_date = parse_datetime(e['date']) if e.get('date') else None
                if event_date and event_date <= now:
                    past_events.append(ContainerEvent(
                        container=container,
                        description=e['description'],
                        date=event_date,
                        is_actual=bool(e.get('isActual')),
                    ))
            ContainerEvent.objects.bulk_create(past_events)
        # print(api_response_data)
        return redirect('shipment_detail', shipment_number = shipment.shipmentNumber)

class ShipmentDetailView(View):
    template_name = 'output.html'
    def get(self, request, shipment_number):
        past_events = Prefetch("containers__events", 
                               queryset=ContainerEvent.objects.filter(
                                   date__lte=django_timezone.now()).order_by("-date"), 
                                   to_attr="past_events",)
        # shipment = get_object_or_404(Shipment, shipmentNumber = shipment_number)
        shipment = get_object_or_404(Shipment.objects.select_related(
            "pol", 
            "pod").prefetch_related("vessels", 
                                    "containers", 
                                    past_events),
            shipmentNumber=shipment_number,)
        return render(request, self.template_name, {"shipment": shipment})