from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPhone Number: {self.phone}"