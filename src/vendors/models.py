from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    email = models.CharField(max_length=120)

    def __str__(self):
        return self.name