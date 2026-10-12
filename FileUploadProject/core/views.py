import json

from django.contrib import messages
from django.db import transaction
from django.shortcuts import redirect, render
from django.views import View

from core.models import Shipment


class HomeView(View):
    template_name = 'home.html'

    def get(self, request):
        # Consume any leftover messages so they don't pile up on the upload page
        list(messages.get_messages(request))
        return render(request, self.template_name)

    def post(self, request):
        uploaded_files = request.FILES.getlist('input_file')
        saved, failed = 0, []

        for file in uploaded_files:
            try:
                json_data = json.loads(file.read().decode("utf-8"))
                meta = json_data["metadata"]
                pol = json_data["route"]["pol"]["location"]
                pod = json_data["route"]["pod"]["location"]

                with transaction.atomic():
                    Shipment.objects.update_or_create(
                        shipmentNumber=meta["shipmentNumber"],
                        defaults={
                            'sealine': meta["sealine"],
                            'route': {
                                'pol': {'name': pol["name"], 'locode': pol["locode"]},
                                'pod': {'name': pod["name"], 'locode': pod["locode"]},
                            },
                            'vessels': [v["name"] for v in json_data.get("vessels", [])],
                        },
                    )
                saved += 1
            except (json.JSONDecodeError, UnicodeDecodeError):
                failed.append(f"{file.name}: not valid JSON")
            except (KeyError, TypeError) as e:
                failed.append(f"{file.name}: missing field {e}")

        # Clear anything old first, then add exactly ONE success message
        list(messages.get_messages(request))
        if saved:
            messages.success(request, f"{saved} file(s) processed successfully!")
        for err in failed:
            messages.error(request, err)

        return redirect('Details')


class DetailView(View):
    template_name = 'detail.html'

    def get(self, request):
        shipments = Shipment.objects.order_by('-updatedAt')
        return render(request, self.template_name, {'shipments': shipments})