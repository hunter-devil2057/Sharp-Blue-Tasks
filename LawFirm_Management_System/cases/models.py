from django.db import models
from clients.models import Client
from lawyers.models import Lawyer

# Create your models here.
class Case(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Open'),
        ('CLOSED', 'Closed'),
        ('PENDING', 'Pending'),
    )
    title = models.CharField(max_length=200)
    description = models. TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models. ForeignKey(Lawyer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title