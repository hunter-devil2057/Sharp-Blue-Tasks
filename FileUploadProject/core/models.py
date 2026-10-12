from django.db import models

class Shipment(models.Model):
    # Shipment Number jahiley ni Unique naii hunxa
    shipmentNumber = models.CharField(max_length=20, unique=True)
    sealine = models.CharField(max_length=10)
    route = models.JSONField(default=dict)
    vessels = models.JSONField(default=list)

    # This fields will be automatically added 
    # When the record is created
    createdAt = models.DateTimeField(auto_now_add=True)
    # When the record is updated
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipmentNumber      # as shipment Number is always unique
    