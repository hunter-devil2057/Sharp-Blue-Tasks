from django.db import models

# Create your models here.
class Lawyer(models.Model) :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str_(self):
        return f"{self.first_name} {self.last_name}"