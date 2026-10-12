from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Port(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=30)
    # Country code xaii only 2 letters ko hunxa
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

    # Details of Port of Loading Date: kaha kun bela xaii load vayo ta?
    pol = models.ForeignKey(Port, on_delete=models.PROTECT, related_name="load_shipments")      # CASCADE vnya delete, PROTECT vnya delete huna nadiney
    # load_shipment: Euta port bata load hune sabai shipments access garne naam.
    # khali ra null hunu vayena
    pol_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    pol_actual = models.BooleanField(default=False)

    # Details of Proof of Delivery: Kaha xaii delivery vayo ta?
    # Kun port ma shipment unload (discharge) hunchha
    pod = models.ForeignKey(Port, on_delete=models.PROTECT, related_name="discharge_shipments")
    pod_date = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    pod_actual = models.BooleanField(default=False)

    # Route Information: Products haru yeuta thau bata aarko thau ma transport garni road/route ko information ho
    # JSONField: JSON bata xaii route segment garxa
    route_data = models.JSONField(default=list, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # model ko configuration ra behavior decide gardinxa
    # Django le Model kashari handle garxa vanera configure garira ho
    # Django ma data kashari handle/organize garni vanera rule define garna 
    class Meta:     
        # object banayera, ORM garda order ma data dinxa
        ordering = ["created_date"]     # created date ko order ma xaii result haru display garni ho 
        # yedi ["-created_date"] gareko vaye descending order ma dinthiyo 

    def __str__(self):
        # Shipment ko object create garera print garda, k display garni????
        return self.shipment_number

    def get_absolute_url(self):
    # provides a convenient way to get the correct detail-page URL for any shipment.
        return reverse("shipment-detail", kwargs={"pk": self.pk})

    @property
    def container_count(self):
        # yesma xaii kati wota containers haru xaan count gardinxa
        return self.containers.count()

class Container(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, related_name="containers")
    number = models.CharField(max_length=20, unique=True)
    isoCode = models.CharField(max_length=10)
    sizeType = models.CharField(max_length=50)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.number

class MetaDataInfo(models.Model):
    shipmentType = models.CharField(max_length=5)
    shipmentNumber = models.CharField(max_length=15)
    sealine = models.CharField(max_length=10)
    sealineName = models.CharField(max_length=100)
    shippingStatus = models.CharField(max_length=20)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipmentNumber