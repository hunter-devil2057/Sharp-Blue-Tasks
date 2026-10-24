from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class Port(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    countryCode = models.CharField(max_length=2)
    # United Nations Code for Trade and Transport Locations.
    # UN/LOCODE vnya xaii Place identify garni unique code raixa, 
    # Max 5 characters = 2 characters for Country + 3 characters for the Location
    # Eg: NPKTM (Kathmandu, Nepal)
    locode = models.CharField(max_length=5, unique=True)

    # Yedi Port Class ko object banayo vnye, str/txt ma kashari dekhauni vanera decide garxa
    def __str__(self):
        return (f"{self.name} {self.locode}")

class Shipment(models.Model):
    shipmentNumber = models.CharField(max_length=20, unique=True)
    shipmentType = models.CharField(max_length=5)
    sealine = models.CharField(max_length=10)
    sealineName = models.CharField(max_length=100)
    shippingStatus = models.CharField(max_length=30)

    # Details of Port of Loading (POL): samaan kun bela xaii load vayo ta?
    pol = models.ForeignKey(Port, on_delete=models.PROTECT, related_name="load_shipments")
    # load_shipment: Euta port bata load huney sabai shipment access garni naam
    pol_date = models.DateTimeField(null=False, blank=False)
    pol_actual = models.BooleanField(default=False)

    # Details of Proof of Delivery (PoD): Kaha xaii Delivery vayo ta?
    # Kun port ma shipment unload (discharge) hunxa
    pod = models.ForeignKey(Port, on_delete=models.PROTECT, related_name="discharge_shipments")
    pod_date = models.DateTimeField(null=False, blank=False)
    pod_actual = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.shipmentNumber

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})

    @property
    def container_count(self):
        return self.containers.count()

    @property
    def vessel_count(self):
        return self.vessels.count()

class Vessel(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="vessels")
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class Container(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="containers")
    number = models.CharField(max_length=20, unique=True)
    isoCode = models.CharField(max_length=10)
    sizeType = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    
    def __str__(self):
        return self.number

class ContainerEvent(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE, related_name="events")
    description = models.CharField(max_length=400)
    date = models.DateTimeField()
    is_actual = models.BooleanField(default = False)

    class Meta:
        ordering = ["date"]
 
    def __str__(self):
        return f"{self.container.number} - {self.description}"
 
    @property
    def time_ago(self):
        seconds = int((timezone.now() - self.date).total_seconds())
        if seconds < 60:
            return "just now"
        minutes = seconds // 60
        if minutes < 60:
            return f"{minutes} min ago"
        hours = minutes // 60
        if hours < 24:
            return f"{hours} hr{'s' if hours != 1 else ''} ago"
        days = hours // 24
        if days < 7:
            return f"{days} day{'s' if days != 1 else ''} ago"
        if days < 30:
            weeks = days // 7
            return f"{weeks} week{'s' if weeks != 1 else ''} ago"
        if days < 365:
            months = days // 30
            return f"{months} month{'s' if months != 1 else ''} ago"
        years = days // 365
        return f"{years} year{'s' if years != 1 else ''} ago"

class MetaDataInfo(models.Model):
    shipmentType = models.CharField(max_length=5)
    shipmentNumber = models.CharField(max_length=15)
    sealine = models.CharField(max_length=10)
    sealineName = models.CharField(max_length=100)
    shippingStatus = models.CharField(max_length=20)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipmentNumber